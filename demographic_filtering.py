import pandas as pd

df=pd.read_csv('articles.csv')
def find_total_events(df1_row):
  total_views=df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "VIEW")].shape[0]
  total_likes=df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "LIKE")].shape[0]
  total_bookmarks=df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "BOOKMARK")].shape[0]
  total_follows=df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "FOLLOW")].shape[0]
  total_comments=df2[(df2["contentId"] == df1_row["contentId"]) & (df2["eventType"] == "COMMENT CREATED")].shape[0]
  return total_views+total_likes+total_bookmarks+total_follows+total_comments

df1["total_events"]=df1.apply(find_total_events,axis=1)

df1=df1.sort_values('total_events',ascending=False)
df1.head(10)