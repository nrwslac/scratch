from dataclasses import dataclass
from typing import Optional, Dict, List
from apischema import deserialize
import json

@dataclass
class Provenance:
    provenance : str

@dataclass
class Duration:
    duration: str

@dataclass
class RelativeTimeRange:
    fromtime: Duration
    totime : Duration

@dataclass
class GrafanaModel:
    alias: str
    aliasPattern : str
    datasource : Dict[str, str]
    functions: list
    intervalMs: int
    maxDataPoints: int
    operator: str
    refId: str
    regex: bool
    stream: bool
    strmcap: str
    strmint: str
    target: str

@dataclass
class AlertQuery:
    datasourceUid : Optional[str]
    model : Optional[GrafanaModel]
    querytype: Optional[str]
    refid: Optional[str]
    relativerimerange: Optional[RelativeTimeRange]

@dataclass
class GrafanaAlert:
    annotations: Optional[Dict[str, str]]
    condition: str
    data: List[AlertQuery]
    execerrstate: str
    folderUID: str
    ford: Duration
    id: Optional[int]
    ispaused: Optional[bool]
    labels: Optional[Dict[str, str]]
    noData: str
    orgID: int
    provenance: Optional[Provenance]
    ruleGroup: str
    title: str
    uid: str
    updated: str

with open("sample_alert.txt", "r") as f:
    alert_json = json.load(f)

alert = deserialize(GrafanaAlert, alert_json)

print(alert)


