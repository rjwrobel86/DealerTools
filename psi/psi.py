import requests
import pandas as pd
links = [LISTOFURLS]
stores = [LISTOFSTORENAMES]

fcps = []
fids = []
lcps = []
clss = []

for i in links:
    x = requests.get("https://www.googleapis.com/pagespeedonline/v5/runPagespeed", params={"url":i,"strategy":"mobile","key":"APIKEYGOESHERE"})
    data = x.json()
        
    fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"] #into seconds (/1000)
    fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"] #into seconds (/1000)
    lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]
    cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]/100
    
    fcps.append(fcp)
    fids.append(fid)
    lcps.append(lcp)
    clss.append(cls)

data = {'First Contentful Paint (MS)':fcps,'First Input Delay (MS)':fids,'Largest Contentful Paint (MS)':lcps,'Cumulative Layout Shift':clss}
df = pd.DataFrame(data, index = stores)
df.head()