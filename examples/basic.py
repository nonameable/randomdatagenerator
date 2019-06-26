import randomdatapy

spec = {
    "columns":[
        {
            "name": "col1"
        },
        {
            "name": "col2"
        }
    ]
}
df = randomdatapy.get_random_df(spec)
print(df)