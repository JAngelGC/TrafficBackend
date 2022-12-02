dataStreets = [
    # Street 0 -> left to right 1
    {
    "start": [0, 47.5],
    "end": [50, 47.5],
    "direction": "right",
    "light": {
        "pos": [44, 44],
        "state": "Green",
        "time": 0,
        } 
    },
    # Street 1 -> left to right 2
    {
    "start": [50, 47.5],
    "end": [100, 47.5],
    "direction": "right",
    "light": {
        "pos": [94, 44],
        "state": "Green",
        "time": 0,
        } 
    },
    # Street 2 -> right to left 1
    {
    "start": [100, 52.5],
    "end": [50, 52.5],
    "direction": "left",
    "light": {
        "pos": [56, 56],
        "state": "Red",
        "time": 150,
        } 
    },
    # Street 3 -> right to left 2
    {
    "start": [50, 52.5],
    "end": [0, 52.5],
    "direction": "left",
    "light": {
        "pos": [6, 56],
        "state": "Red",
        "time": 150,
        } 
    },

    # Street 4 -> down to up 1
    {
    "start": [52.5, 0],
    "end": [52.5, 50],
    "direction": "up",
    "light": {
        "pos": [56, 44],
        "state": "Red",
        "time": 100,
        } 
    },
    # Street 5 -> down to up 2
    {
    "start": [52.5, 50],
    "end": [52.5, 100],
    "direction": "up",
    "light": {
        "pos": [56, 94],
        "state": "Green",
        "time": 0,
        } 
    },
    # Street 6 -> up to down 1
    {
    "start": [47.5, 100],
    "end": [47.5, 50],
    "direction": "down",
    "light": {
        "pos": [44, 56],
        "state": "Red",
        "time": 50,
        } 
    },
    # Street 7 -> up to down 2
    {
    "start": [47.5, 50],
    "end": [47.5, 0],
    "direction": "down",
    "light": {
        "pos": [44, 6],
        "state": "Red",
        "time": 150,
        } 
    },


    # Outside streets ----------------------------------------

    # Street 8 -> left to right
    {
    "start": [0, 97.5],
    "end": [50, 97.5],
    "direction": "right",
    "light": {
        "pos": [44, 94],
        "state": "Red",
        "time": 50,
        } 
    },

    # Street 9 -> left to right
    {
    "start": [50, 97.5],
    "end": [100, 97.5],
    "direction": "right",
    "light": {
        "state": "White"
        } 
    },

    # Street 10 -> up to down
    {
    "start": [97.5, 100],
    "end": [97.5, 50],
    "direction": "down",
    "light": {
        "pos": [94, 56],
        "state": "Red",
        "time": 50,
        } 
    },

    # Street 11 -> up to down
    {
    "start": [97.5, 50],
    "end": [97.5, 0],
    "direction": "down",
    "light": {
        "state": "White"
        } 
    },

    # Street 12 -> right to left
    {
    "start": [100, 2.5],
    "end": [50, 2.5],
    "direction": "left",
    "light": {
        "pos": [56, 6],
        "state": "Red",
        "time": 100,
        } 
    },

    # Street 13 -> right to left
    {
    "start": [50, 2.5],
    "end": [0, 2.5],
    "direction": "left",
    "light": {
        "state": "White"
        } 
    },

    # Street 14 -> down to up
    {
    "start": [2.5, 0],
    "end": [2.5, 50],
    "direction": "up",
    "light": {
        "pos": [6, 44],
        "state": "Red",
        "time": 100,
        } 
    },

    # Street 15 -> down to up
    {
    "start": [2.5, 50],
    "end": [2.5, 100],
    "direction": "up",
    "light": {
        "state": "White"
        } 
    },
]


dataCars = [

    # street 0
    {
        "pos": [15, 47.5],
        "speed": [1, 0],
        "street": 0,
    },
    {
        "pos": [25, 47.5],
        "speed": [1, 0],
        "street": 0,
    },
    {
        "pos": [35, 47.5],
        "speed": [1, 0],
        "street": 0,
    },

    # street 1
    {
        "pos": [65, 47.5],
        "speed": [1, 0],
        "street": 1,
    },

    # street 2
    {
        "pos": [65, 52.5],
        "speed": [-1, 0],
        "street": 2,
    },
    {
        "pos": [85, 52.5],
        "speed": [-1, 0],
        "street": 2,
    },

    # street 3
    {
        "pos": [15, 52.5],
        "speed": [-1, 0],
        "street": 3,
    },
    {
        "pos": [35, 52.5],
        "speed": [-1, 0],
        "street": 3,
    },

    # street 4
    {
        "pos": [52.5, 10],
        "speed": [0, 1],
        "street": 4,
    },
    {
        "pos": [52.5, 20],
        "speed": [0, 1],
        "street": 4,
    },
    {
        "pos": [52.5, 35],
        "speed": [0, 1],
        "street": 4,
    },

    # street 5
    {
        "pos": [52.5, 55],
        "speed": [0, 1],
        "street": 5,
    },

    # street 6
    {
        "pos": [47.5, 65],
        "speed": [0, -1],
        "street": 6,
    },
    {
        "pos": [47.5, 85],
        "speed": [0, -1],
        "street": 6,
    },

    # street 7
    {
        "pos": [47.5, 40],
        "speed": [0, -1],
        "street": 7,
    },
    {
        "pos": [47.5, 20],
        "speed": [0, -1],
        "street": 7,
    },

    # street 8
    {
        "pos": [20, 97.5],
        "speed": [1, 0],
        "street": 8,
    },

    # street 9
    {
        "pos": [70, 97.5],
        "speed": [1, 0],
        "street": 9,
    },

    # street 10
    {
        "pos": [97.5, 70],
        "speed": [0, -1],
        "street": 10,
    },

    # street 11
    {
        "pos": [97.5, 30],
        "speed": [0, -1],
        "street": 11,
    },

    # street 12
    {
        "pos": [65, 2.5],
        "speed": [-1, 0],
        "street": 12,
    },

    # street 13
    {
        "pos": [35, 2.5],
        "speed": [-1, 0],
        "street": 13,
    },

    # street 14
    {
        "pos": [2.5, 15],
        "speed": [0, 1],
        "street": 14,
    },

    # street 15
    {
        "pos": [2.5, 65],
        "speed": [0, 1],
        "street": 15,
    },


]


dataSetStreets = [
    #left forward right
    {
        "id": 0 ,
        "info": [5, 1, 7]
    },
    {
        "id": 1 ,
        "info": [None, 0, 11]
    },
    {
        "id": 2 ,
        "info": [7, 3, 5]
    },
    {
        "id": 3 ,
        "info": [None, 2, 15]
    },
    {
        "id": 4 ,
        "info": [3, 5, 1]
    },
    {
        "id": 5 ,
        "info": [None, 4, 9]
    },
    {
        "id": 6 ,
        "info": [1, 7, 3]
    },
    {
        "id": 7 ,
        "info": [None, 6, 13]
    },
    
    # Outside streets:
    #left forward right
    {
        "id": 8 ,
        "info": [4, 9, 6]
    },
    {
        "id": 9 ,
        "info": [None, None, 10]
    },
    {
        "id": 10 ,
        "info": [0, 11, 2]
    },
    {
        "id": 11 ,
        "info": [None, None, 12]
    },
    {
        "id": 12 ,
        "info": [6, 13, 4]
    },
    {
        "id": 13 ,
        "info": [None, None, 14]
    },
    {
        "id": 14 ,
        "info": [2, 15, 0]
    },
    {
        "id": 15 ,
        "info": [None, None, 8]
    },

]

