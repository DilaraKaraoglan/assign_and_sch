# data/build_data.py

def build_item_map():
    return {
    
    # Racks 1–3 → FLEXIBLE (weight=1)
    
    # Racks 1
    "i1":  (1, 3,  "L", 1),
    "i2":  (1, 7,  "R", 1),
    "i3":  (1, 11, "L", 1),
    "i4":  (1, 14, "R", 1),
    "i5":  (1, 18, "L", 1),
    "i6":  (1, 22, "R", 1),
    "i7":  (1, 26, "L", 1),
    "i8":  (1, 29, "R", 1),
    
    # Racks 2
    "i9":  (2, 2,  "L", 1),
    "i10": (2, 6,  "R", 1),
    "i11": (2, 10, "L", 1),
    "i12": (2, 14, "R", 1),
    "i13": (2, 17, "L", 1),
    "i14": (2, 21, "R", 1),
    "i15": (2, 25, "L", 1),
    "i16": (2, 28, "R", 1),
    
    # Racks 3
    "i17": (3, 4,  "L", 1),
    "i18": (3, 8,  "R", 1),
    "i19": (3, 12, "L", 1),
    "i20": (3, 14, "R", 1),
    "i21": (3, 19, "L", 1),
    "i22": (3, 23, "R", 1),
    "i23": (3, 27, "L", 1),
    "i24": (3, 30, "R", 1),
    
    
    # Racks 4–11 → HUMAN_ONLY (weight=0)
    
    # Aisle 4
    "i25": (4, 3,  "L", 0),
    "i26": (4, 7,  "R", 0),
    "i27": (4, 11, "L", 0),
    "i28": (4, 14, "R", 0),
    "i29": (4, 18, "L", 0),
    "i30": (4, 22, "R", 0),
    "i31": (4, 26, "L", 0),
    "i32": (4, 29, "R", 0),
    
    # Racks 5
    "i33": (5, 2,  "L", 0),
    "i34": (5, 6,  "R", 0),
    "i35": (5, 10, "L", 0),
    "i36": (5, 14, "R", 0),
    "i37": (5, 17, "L", 0),
    "i38": (5, 21, "R", 0),
    "i39": (5, 25, "L", 0),
    "i40": (5, 28, "R", 0),
    
    # Racks 6
    "i41": (6, 4,  "L", 0),
    "i42": (6, 8,  "R", 0),
    "i43": (6, 12, "L", 0),
    "i44": (6, 14, "R", 0),
    "i45": (6, 19, "L", 0),
    "i46": (6, 23, "R", 0),
    "i47": (6, 27, "L", 0),
    "i48": (6, 30, "R", 0),
    
    # Racks 7
    "i49": (7, 3,  "L", 0),
    "i50": (7, 7,  "R", 0),
    "i51": (7, 11, "L", 0),
    "i52": (7, 14, "R", 0),
    "i53": (7, 18, "L", 0),
    "i54": (7, 22, "R", 0),
    "i55": (7, 26, "L", 0),
    "i56": (7, 29, "R", 0),
    
    # Racks 8
    "i57": (8, 2,  "L", 0),
    "i58": (8, 6,  "R", 0),
    "i59": (8, 10, "L", 0),
    "i60": (8, 14, "R", 0),
    "i61": (8, 17, "L", 0),
    "i62": (8, 21, "R", 0),
    "i63": (8, 25, "L", 0),
    "i64": (8, 28, "R", 0),
    
    # Racks 9
    "i65": (9, 4,  "L", 0),
    "i66": (9, 8,  "R", 0),
    "i67": (9, 12, "L", 0),
    "i68": (9, 14, "R", 0),
    "i69": (9, 19, "L", 0),
    "i70": (9, 23, "R", 0),
    "i71": (9, 27, "L", 0),
    "i72": (9, 30, "R", 0),
    
    # Racks 10
    "i73": (10, 3,  "L", 0),
    "i74": (10, 7,  "R", 0),
    "i75": (10, 11, "L", 0),
    "i76": (10, 14, "R", 0),
    "i77": (10, 18, "L", 0),
    "i78": (10, 22, "R", 0),
    "i79": (10, 26, "L", 0),
    "i80": (10, 29, "R", 0),
    

    }
def build_pallets():

    return [

        # FLEXIBLE (1–25)
        {"pallet_id":"P1","items":[{"item_id":"i1","qty":2},{"item_id":"i2","qty":1}]},
        {"pallet_id":"P2","items":[{"item_id":"i3","qty":1},{"item_id":"i4","qty":2}]},
        {"pallet_id":"P3","items":[{"item_id":"i5","qty":1},{"item_id":"i6","qty":1}]},
        {"pallet_id":"P4","items":[{"item_id":"i7","qty":2},{"item_id":"i8","qty":1}]},
        {"pallet_id":"P5","items":[{"item_id":"i9","qty":1},{"item_id":"i10","qty":2}]},

        {"pallet_id":"P6","items":[{"item_id":"i11","qty":1},{"item_id":"i12","qty":1}]},
        {"pallet_id":"P7","items":[{"item_id":"i13","qty":2},{"item_id":"i14","qty":1}]},
        {"pallet_id":"P8","items":[{"item_id":"i15","qty":1},{"item_id":"i16","qty":1}]},
        {"pallet_id":"P9","items":[{"item_id":"i17","qty":2},{"item_id":"i15","qty":1}]},
        {"pallet_id":"P10","items":[{"item_id":"i19","qty":1},{"item_id":"i14","qty":2}]},

        {"pallet_id":"P11","items":[{"item_id":"i1","qty":1},{"item_id":"i11","qty":1}]},
        {"pallet_id":"P12","items":[{"item_id":"i3","qty":1},{"item_id":"i13","qty":1}]},
        {"pallet_id":"P13","items":[{"item_id":"i5","qty":1},{"item_id":"i15","qty":1}]},
        {"pallet_id":"P14","items":[{"item_id":"i7","qty":1},{"item_id":"i17","qty":1}]},
        {"pallet_id":"P15","items":[{"item_id":"i9","qty":1},{"item_id":"i19","qty":1}]},

        {"pallet_id":"P16","items":[{"item_id":"i2","qty":1},{"item_id":"i12","qty":1}]},
        {"pallet_id":"P17","items":[{"item_id":"i4","qty":1},{"item_id":"i14","qty":1}]},
        {"pallet_id":"P18","items":[{"item_id":"i6","qty":1},{"item_id":"i16","qty":1}]},
        {"pallet_id":"P19","items":[{"item_id":"i8","qty":1},{"item_id":"i10","qty":1}]},
        {"pallet_id":"P20","items":[{"item_id":"i10","qty":1},{"item_id":"i12","qty":1}]},

        {"pallet_id":"P21","items":[{"item_id":"i21","qty":1},{"item_id":"i23","qty":1}]},
        {"pallet_id":"P22","items":[{"item_id":"i23","qty":2},{"item_id":"i1","qty":1}]},
        {"pallet_id":"P23","items":[{"item_id":"i17","qty":1},{"item_id":"i3","qty":1}]},
        {"pallet_id":"P24","items":[{"item_id":"i21","qty":1},{"item_id":"i5","qty":1}]},
        {"pallet_id":"P25","items":[{"item_id":"i23","qty":1},{"item_id":"i7","qty":1}]},

        # HUMAN_ONLY (26–50)
        {"pallet_id":"P26","items":[{"item_id":"i25","qty":2},{"item_id":"i26","qty":1}]},
        {"pallet_id":"P27","items":[{"item_id":"i27","qty":1},{"item_id":"i28","qty":1}]},
        {"pallet_id":"P28","items":[{"item_id":"i29","qty":2},{"item_id":"i30","qty":1}]},
        {"pallet_id":"P29","items":[{"item_id":"i41","qty":1},{"item_id":"i42","qty":1}]},
        {"pallet_id":"P30","items":[{"item_id":"i43","qty":2},{"item_id":"i44","qty":1}]},

        {"pallet_id":"P31","items":[{"item_id":"i45","qty":1},{"item_id":"i46","qty":1}]},
        {"pallet_id":"P32","items":[{"item_id":"i49","qty":2},{"item_id":"i50","qty":1}]},
        {"pallet_id":"P33","items":[{"item_id":"i51","qty":1},{"item_id":"i52","qty":1}]},
        {"pallet_id":"P34","items":[{"item_id":"i53","qty":2},{"item_id":"i54","qty":1}]},
        {"pallet_id":"P35","items":[{"item_id":"i65","qty":1},{"item_id":"i66","qty":1}]},

        {"pallet_id":"P36","items":[{"item_id":"i67","qty":2},{"item_id":"i68","qty":1}]},
        {"pallet_id":"P37","items":[{"item_id":"i69","qty":1},{"item_id":"i70","qty":1}]},
        {"pallet_id":"P38","items":[{"item_id":"i17","qty":2},{"item_id":"i59","qty":1}]},
        {"pallet_id":"P39","items":[{"item_id":"i4","qty":1},{"item_id":"i47","qty":1}]},
        {"pallet_id":"P40","items":[{"item_id":"i5","qty":2},{"item_id":"i79","qty":1}]},

        {"pallet_id":"P41","items":[{"item_id":"i25","qty":1},{"item_id":"i41","qty":1}]},
        {"pallet_id":"P42","items":[{"item_id":"i27","qty":1},{"item_id":"i43","qty":1}]},
        {"pallet_id":"P43","items":[{"item_id":"i29","qty":1},{"item_id":"i45","qty":1}]},
        {"pallet_id":"P44","items":[{"item_id":"i49","qty":1},{"item_id":"i65","qty":1}]},
        {"pallet_id":"P45","items":[{"item_id":"i51","qty":1},{"item_id":"i67","qty":1}]},
        {"pallet_id":"P46","items":[{"item_id":"i53","qty":1},{"item_id":"i69","qty":1}]},
        {"pallet_id":"P47","items":[{"item_id":"i31","qty":1},{"item_id":"i56","qty":1}]},
        {"pallet_id":"P48","items":[{"item_id":"i73","qty":1},{"item_id":"i25","qty":1}]},
        {"pallet_id":"P49","items":[{"item_id":"i41","qty":1},{"item_id":"i27","qty":1}]},
        {"pallet_id":"P50","items":[{"item_id":"i43","qty":1},{"item_id":"i29","qty":1}]},
    ]

def build_agents():

    agents = []

    # 10 human
    for i in range(10):
        agents.append({
            "id": i,
            "type": "human",
            "speed": 1.3,
            "pickTime": 21.0
        })

    # 3 robot
    for i in range(10, 13):
        agents.append({
            "id": i,
            "type": "robot",
            "speed": 0.9,
            "pickTime": 40.0
        })

    return agents


def build_search_time():
    return {
        "human": 1.0,
        "robot": 0.0
    }