x=[
    [40,12,56],
    [59,78,16],
    [58,69,37]
]
y=[
    [40,12,56],
    [59,78,16],
    [58,69,37]
]
results=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(x)):
    for j in range(len(x[0])):
        results [i][j]=x[i][j]/y[i][j]
for r in results:
    print(r)