

"""
 
df=pd.read_json("celeblinks.json") # your json files
print(df.shape) # 4900 image


duplicated_count1 = df.duplicated('urlname').sum()
duplicated_count2 = df.duplicated('imgname').sum()


print(duplicated_count1)
print( duplicated_count2)

if there are duplicated values :
    df.drop_duplicates('image_url', keep='first', inplace=True)
    df.drop_duplicates('image_name', keep='first', inplace=True)

    """