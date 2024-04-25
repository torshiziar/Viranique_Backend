import re
from device.models import Sensor
import datetime
from datetime import timedelta
from Angizeh_2 import influx_client
client = influx_client.connection()

pk=2793
sensor = Sensor.objects.filter(pk=pk)
sensor = sensor.first()
topic = sensor.value_topic
duration_from=datetime.datetime.now()-timedelta(days=10)
duration_to=datetime.datetime.now()
part_no, gate, type = re.findall("/angizeh/(.*)/(.*)/(.*)", topic)[0]
# timestamp='v.windowPeriod'
timestamp='5m'
mean_query = f"""
            from(bucket:"mqtt.angizehco.com")\n
            |> range(start: {duration_from.strftime('%Y-%m-%dT%H:%M:%SZ')}, stop: {duration_to.strftime('%Y-%m-%dT%H:%M:%SZ')}) 
            |> filter(fn: (r) => r["_measurement"] == "{type}")
            |> filter(fn: (r) => r["part_number"] == "{part_no}")
            |> filter(fn: (r) => r["gateway"] == "{gate}")
            |> aggregateWindow(every: {timestamp}, fn: mean, createEmpty: false)
            |> yield(name: "mean_value")\n"""


query_api = client.query_api()

results = query_api.query_data_frame(mean_query)
# logger.debug(results)
responses = []
if isinstance(results, list):
    for i in range(len(results)):
        results[i] = results[i][["_time", "_value"]].rename(columns={"_time": "time", "_value": results[i]["result"][0]})
        results[i] = results[i].set_index('time').tz_convert("Asia/Tehran").reset_index().sort_values('time')
        if i > 0:
            results[i] = pd.merge_asof(results[i-1], results[i], on="time",)
    records = results[-1].to_dict(orient='records')
    responses.append({sensor[0].id: records})
elif not results.empty:
    results = results[["_time", "_value"]].rename(columns={"_time": "time", "_value": results["result"][0]})
    results = results.set_index('time').tz_convert("Asia/Tehran").reset_index().sort_values('time')
    records = results.to_dict(orient='records')
    responses.append({sensor.id: records})
else:
    responses.append({sensor.id: []})
