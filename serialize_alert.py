from dataclasses import dataclass, field
from typing import Optional, Dict, List
from apischema import deserialize, alias, serialize
import json

@dataclass
class Evaluator:
    params: List[int] = field(default_factory=list) 
    type_: str = field(metadata=alias("type"), default="")

@dataclass
class Operator:
    type_: str = field(metadata=alias("type"), default="")

@dataclass
class Query:
    params: List[str] = field(default_factory=list)

@dataclass
class Reducer:
    type_: str = field(metadata=alias("type"), default="")

@dataclass
class Provenance:
    provenance : str

@dataclass
class RelativeTimeRange:
    from_: int = field(metadata=alias("from"), default=0)
    to: int = field(default=0)

@dataclass
class GrafanaModel:
    alias_: Optional[str] = field(metadata=alias("alias"), default="")
    aliasPattern : str = ""
    conditions: Optional[List] = field(default_factory=lambda: [Evaluator(), Operator(), Query(), Reducer()])
    datasource : Dict[str, str] = field(default_factory=dict)
    functions: list = field(default_factory=list)
    intervalMs: int = 0
    maxDataPoints: int = 0 
    operator: str = ""
    refId: str = ""
    regex: bool = False
    stream: bool = False
    strmCap: str = ""
    strmInt: str = ""
    target: str = ""
    type_: Optional[str] = field(metadata=alias("type"), default="")


@dataclass
class AlertQuery:
    datasourceUid : Optional[str]
    model : Optional[GrafanaModel]
    queryType: Optional[str]
    refId: Optional[str]
    relativeTimeRange: Optional[RelativeTimeRange]

@dataclass
class GrafanaAlert:
    annotations: Optional[Dict[str, str]] = field(default_factory=lambda:{}) 
    condition: str = ""
    data: List[AlertQuery] = field(default_factory=lambda:[])
    execErrState: str = ""
    folderUID: str = ""
    for_: str = field(metadata=alias("for"), default="")
    id_: Optional[int] = field(metadata=alias("id"), default=None)
    isPaused: Optional[bool] = None
    labels: Optional[Dict[str, str]] = field(default_factory=lambda:{}) 
    noDataState: str = ""
    notification_settings: Optional[None] = field(default=None)
    orgID: int = ""
    provenance: Optional[Provenance] = field(default=None) 
    record: Optional[None] = field(default=None)
    ruleGroup: str = ""
    title: str = ""
    uid: str = ""
    updated: str = ""

#with open("sample_alert.txt", "r") as f:
    #alert_json = json.load(f)

#alert = deserialize(GrafanaAlert, alert_json)

#print(alert)
'''
with open("sample_time.json", "r") as f:
    time_json = json.load(f)
time_json_object = time_json.get("relativeTimeRange", {})
time = deserialize(RelativeTimeRange, time_json_object)
print(time)

with open("sample_model.json", "r") as f:
    model_json = json.load(f)
model_json_object = model_json.get("model", {})
model = deserialize(GrafanaModel, model_json_object)
print(model)

with open("sample_alert_query.json", "r") as f:
    alert_json = json.load(f)
alert_json_object = alert_json.get("data", {})
l = list(alert_json_object)
alert_q = deserialize(AlertQuery, l[0])
print(alert_q)
'''

with open("sample_alert.json", "r") as f:
    alert_json = json.load(f)
alert = deserialize(GrafanaAlert, alert_json)
print(alert)


with open("sample_alert_serialize.json", "w") as f:
    alert = serialize(GrafanaAlert, alert)
    f.write(json.dumps(alert))