from pulumi_kubernetes.helm.v2 import Chart, LocalChartOpts
from yaml import load, dump

mesh = Chart(
    "istio",
    LocalChartOpts(
        path="./istio-1.1.3/install/kubernetes/helm/istio/",
        namespace="istio-system",
        values=dump("./istio-1.1.3/install/kubernetes/helm/istio/values.yaml")
    )
)
