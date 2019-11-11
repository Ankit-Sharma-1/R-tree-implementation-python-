import csv
import time

def MBR(input_coordinates):
    min_x = 100000
    max_x = 0
    min_y = 100000
    max_y = 0
    
    for p in input_coordinates:
        x, y = p
        if x < min_x:
            min_x = x

    for p in input_coordinates:
        x, y = p
        if x > max_x:
            max_x = x


    for p in input_coordinates:
        x, y = p
        if y < min_y:
            min_y = y

    for p in input_coordinates:
        x, y = p
        if y > max_y:
            max_y = y

    mbr = [min_x,max_x,min_y,max_y]
    return(mbr)


def brute_force_range_query(range_query):
    i = 0
    x1, x2, y1, y2 = range_query
    for point in Data_points:
        x, y = point
        if x1 <= x and x <= x2 and y1 <= y and y <= y2:
            i+= 1
    return(i)

def is_intersecting(range_query,mbr):
    x1, x2, y1, y2 = mbr
    l1, l2, m1, m2 = range_query
    if (x1 > l2 or x2 < l1):
        return False

    if (y2 < m1 or y1 > m2):
        return False
        
    return True

def is_bounding(range_query,mbr):
    x1, x2, y1, y2 = mbr
    l1, l2, m1, m2 = range_query
    return (y1 < m1 and x1 < l1 and y2 > m2 and x2 > l2)

def r_tree_algorithm(range_query,dict_root_MBR,dict_level1_child_MBR,dict_level2_child_MBR,dict_leaf_MBR,dict_leaf):
    i = 0
    x1, x2, y1, y2 = range_query
    for p in dict_root_MBR:
        if is_intersecting(range_query,dict_root_MBR[p]) == True or is_bounding(range_query,dict_root_MBR[p]) == True:
            level_1 = ((p*10)-9)
            max_level_1 = (p*10)
            while level_1 <= max_level_1:
                if is_intersecting(range_query,dict_level1_child_MBR[level_1]) == True or is_bounding(range_query,dict_level1_child_MBR[level_1]) == True:
                    level_2 = ((level_1*10)-9)
                    max_level_2 = (level_1*10)
                    while level_2 <= max_level_2:
                        if is_intersecting(range_query,dict_level2_child_MBR[level_2]) == True or is_bounding(range_query,dict_level2_child_MBR[level_2]) == True:
                            node = ((level_2*10)-9)
                            max_node = (level_2*10)                            
                            while node <= max_node:
                                if is_intersecting(range_query,dict_leaf_MBR[node]) == True or is_bounding(range_query,dict_leaf_MBR[node]) == True:
                                    for point in dict_leaf[node]:
                                        x, y = point
                                        if x1 <= x and x <= x2 and y1 <= y and y <= y2:
                                            i+= 1
                                node += 1
                        level_2 += 1
                level_1 += 1    
    return(i)
    
# Store input 100,000 points in list Data_points
reader = csv.reader(open("Data.csv", "r"))
Data_points = []
for row in reader:
    key, x, y = row    
    Data_points.append((int(x),int(y)))

# Create R tree using sort tile recursive algorithm

"""
Assumptions :
Total data points (D) = 100,000
Maximum number of elements stored in a leaf (M)= 10

Sort-Tile-Recursive Algorithm :
1. Order data points in  = 10000 [D/M] consecutive groups of 10 data points
   Each group of M points will be placed in same leaf level node    
2. Load the 1000 [D/M] groups of rectangles into pages
   Store the (MBR, page-number) for each leaf level page into a temporary location
   The page-nulnbers are used as the child pointers in the nodes of the next higher level
3. Recursively pack MBRs into nodes at the next level, proceeding upwards, till root node

Ordering of datapoints
1. The datapoints are sorted by x coordinate and data space is tiled to have "sqrt(D/M)" nodes 
2. As D is 100,000 and M is 10 the data space is tiled into 100 vertical slices (sqrt(D/M))
3. Points in each slice are sorted by y coordinated and packed in nodes of length M (10)

"""
# Sort data points by x and y coordinate
Data_points_sorted = sorted(Data_points , key=lambda k: [k[0], k[1]])

# Creating 100 slices
Slice_1 = []
Slice_2 = []
Slice_3 = []
Slice_4 = []
Slice_5 = []
Slice_6 = []
Slice_7 = []
Slice_8 = []
Slice_9 = []
Slice_10 = []
Slice_11 = []
Slice_12 = []
Slice_13 = []
Slice_14 = []
Slice_15 = []
Slice_16 = []
Slice_17 = []
Slice_18 = []
Slice_19 = []
Slice_20 = []
Slice_21 = []
Slice_22 = []
Slice_23 = []
Slice_24 = []
Slice_25 = []
Slice_26 = []
Slice_27 = []
Slice_28 = []
Slice_29 = []
Slice_30 = []
Slice_31 = []
Slice_32 = []
Slice_33 = []
Slice_34 = []
Slice_35 = []
Slice_36 = []
Slice_37 = []
Slice_38 = []
Slice_39 = []
Slice_40 = []
Slice_41 = []
Slice_42 = []
Slice_43 = []
Slice_44 = []
Slice_45 = []
Slice_46 = []
Slice_47 = []
Slice_48 = []
Slice_49 = []
Slice_40 = []
Slice_41 = []
Slice_42 = []
Slice_43 = []
Slice_44 = []
Slice_45 = []
Slice_46 = []
Slice_47 = []
Slice_48 = []
Slice_49 = []
Slice_50 = []
Slice_51 = []
Slice_52 = []
Slice_53 = []
Slice_54 = []
Slice_55 = []
Slice_56 = []
Slice_57 = []
Slice_58 = []
Slice_59 = []
Slice_60 = []
Slice_61 = []
Slice_62 = []
Slice_63 = []
Slice_64 = []
Slice_65 = []
Slice_66 = []
Slice_67 = []
Slice_68 = []
Slice_69 = []
Slice_70 = []
Slice_71 = []
Slice_72 = []
Slice_73 = []
Slice_74 = []
Slice_75 = []
Slice_76 = []
Slice_77 = []
Slice_78 = []
Slice_79 = []
Slice_80 = []
Slice_81 = []
Slice_82 = []
Slice_83 = []
Slice_84 = []
Slice_85 = []
Slice_86 = []
Slice_87 = []
Slice_88 = []
Slice_89 = []
Slice_90 = []
Slice_91 = []
Slice_92 = []
Slice_93 = []
Slice_94 = []
Slice_95 = []
Slice_96 = []
Slice_97 = []
Slice_98 = []
Slice_99 = []
Slice_100 = []


for k in Data_points_sorted:
    x, y = k
    if x >= 0 and x < 1000:
        Slice_1.append(k)
    elif x >= 1000 and x < 2000:
        Slice_2.append(k)
    elif x >= 2000 and x < 3000:
        Slice_3.append(k)
    elif x >= 3000 and x < 4000:
        Slice_4.append(k)
    elif x >= 4000 and x < 5000:
        Slice_5.append(k)
    elif x >= 5000 and x < 6000:
        Slice_6.append(k)
    elif x >= 6000 and x < 7000:
        Slice_7.append(k)
    elif x >= 7000 and x < 8000:
        Slice_8.append(k)
    elif x >= 8000 and x < 9000:
        Slice_9.append(k)
    elif x >= 9000 and x < 10000:
        Slice_10.append(k)
    elif x >= 10000 and x < 11000:
        Slice_11.append(k)
    elif x >= 11000 and x < 12000:
        Slice_12.append(k)
    elif x >= 12000 and x < 13000:
        Slice_13.append(k)
    elif x >= 13000 and x < 14000:
        Slice_14.append(k)
    elif x >= 14000 and x < 15000:
        Slice_15.append(k)
    elif x >= 15000 and x < 16000:
        Slice_16.append(k)
    elif x >= 16000 and x < 17000:
        Slice_17.append(k)
    elif x >= 17000 and x < 18000:
        Slice_18.append(k)
    elif x >= 18000 and x < 19000:
        Slice_19.append(k)
    elif x >= 19000 and x < 20000:
        Slice_20.append(k)
    elif x >= 20000 and x < 21000:
        Slice_21.append(k)
    elif x >= 21000 and x < 22000:
        Slice_22.append(k)
    elif x >= 22000 and x < 23000:
        Slice_23.append(k)
    elif x >= 23000 and x < 24000:
        Slice_24.append(k)
    elif x >= 24000 and x < 25000:
        Slice_25.append(k)
    elif x >= 25000 and x < 26000:
        Slice_26.append(k)
    elif x >= 26000 and x < 27000:
        Slice_27.append(k)
    elif x >= 27000 and x < 28000:
        Slice_28.append(k)
    elif x >= 28000 and x < 29000:
        Slice_29.append(k)
    elif x >= 29000 and x < 30000:
        Slice_30.append(k)
    elif x >= 30000 and x < 31000:
        Slice_31.append(k)
    elif x >= 31000 and x < 32000:
        Slice_32.append(k)
    elif x >= 32000 and x < 33000:
        Slice_33.append(k)
    elif x >= 33000 and x < 34000:
        Slice_34.append(k)
    elif x >= 34000 and x < 35000:
        Slice_35.append(k)
    elif x >= 35000 and x < 36000:
        Slice_36.append(k)
    elif x >= 36000 and x < 37000:
        Slice_37.append(k)
    elif x >= 37000 and x < 38000:
        Slice_38.append(k)
    elif x >= 38000 and x < 39000:
        Slice_39.append(k)
    elif x >= 39000 and x < 40000:
        Slice_40.append(k)
    elif x >= 40000 and x < 41000:
        Slice_41.append(k)
    elif x >= 41000 and x < 42000:
        Slice_42.append(k)
    elif x >= 42000 and x < 43000:
        Slice_43.append(k)
    elif x >= 43000 and x < 44000:
        Slice_44.append(k)
    elif x >= 44000 and x < 45000:
        Slice_45.append(k)
    elif x >= 45000 and x < 46000:
        Slice_46.append(k)
    elif x >= 46000 and x < 47000:
        Slice_47.append(k)
    elif x >= 47000 and x < 48000:
        Slice_48.append(k)
    elif x >= 48000 and x < 49000:
        Slice_49.append(k)
    elif x >= 49000 and x < 50000:
        Slice_50.append(k)
    elif x >= 50000 and x < 51000:
        Slice_51.append(k)
    elif x >= 51000 and x < 52000:
        Slice_52.append(k)
    elif x >= 52000 and x < 53000:
        Slice_53.append(k)
    elif x >= 53000 and x < 54000:
        Slice_54.append(k)
    elif x >= 54000 and x < 55000:
        Slice_55.append(k)
    elif x >= 55000 and x < 56000:
        Slice_56.append(k)
    elif x >= 56000 and x < 57000:
        Slice_57.append(k)
    elif x >= 57000 and x < 58000:
        Slice_58.append(k)
    elif x >= 58000 and x < 59000:
        Slice_59.append(k)
    elif x >= 59000 and x < 60000:
        Slice_60.append(k)
    elif x >= 60000 and x < 61000:
        Slice_61.append(k)
    elif x >= 61000 and x < 62000:
        Slice_62.append(k)
    elif x >= 62000 and x < 63000:
        Slice_63.append(k)
    elif x >= 63000 and x < 64000:
        Slice_64.append(k)
    elif x >= 64000 and x < 65000:
        Slice_65.append(k)
    elif x >= 65000 and x < 66000:
        Slice_66.append(k)
    elif x >= 66000 and x < 67000:
        Slice_67.append(k)
    elif x >= 67000 and x < 68000:
        Slice_68.append(k)
    elif x >= 68000 and x < 69000:
        Slice_69.append(k)
    elif x >= 69000 and x < 70000:
        Slice_70.append(k)
    elif x >= 70000 and x < 71000:
        Slice_71.append(k)
    elif x >= 71000 and x < 72000:
        Slice_72.append(k)
    elif x >= 72000 and x < 73000:
        Slice_73.append(k)
    elif x >= 73000 and x < 74000:
        Slice_74.append(k)
    elif x >= 74000 and x < 75000:
        Slice_75.append(k)
    elif x >= 75000 and x < 76000:
        Slice_76.append(k)
    elif x >= 76000 and x < 77000:
        Slice_77.append(k)
    elif x >= 77000 and x < 78000:
        Slice_78.append(k)
    elif x >= 78000 and x < 79000:
        Slice_79.append(k)
    elif x >= 79000 and x < 80000:
        Slice_80.append(k)
    elif x >= 80000 and x < 81000:
        Slice_81.append(k)
    elif x >= 81000 and x < 82000:
        Slice_82.append(k)
    elif x >= 82000 and x < 83000:
        Slice_83.append(k)
    elif x >= 83000 and x < 84000:
        Slice_84.append(k)
    elif x >= 84000 and x < 85000:
        Slice_85.append(k)
    elif x >= 85000 and x < 86000:
        Slice_86.append(k)
    elif x >= 86000 and x < 87000:
        Slice_87.append(k)
    elif x >= 87000 and x < 88000:
        Slice_88.append(k)
    elif x >= 88000 and x < 89000:
        Slice_89.append(k)
    elif x >= 89000 and x < 90000:
        Slice_90.append(k)
    elif x >= 90000 and x < 91000:
        Slice_91.append(k)
    elif x >= 91000 and x < 92000:
        Slice_92.append(k)
    elif x >= 92000 and x < 93000:
        Slice_93.append(k)
    elif x >= 93000 and x < 94000:
        Slice_94.append(k)
    elif x >= 94000 and x < 95000:
        Slice_95.append(k)
    elif x >= 95000 and x < 96000:
        Slice_96.append(k)
    elif x >= 96000 and x < 97000:
        Slice_97.append(k)
    elif x >= 97000 and x < 98000:
        Slice_98.append(k)
    elif x >= 98000 and x < 99000:
        Slice_99.append(k)
    elif x >= 99000:
        Slice_100.append(k)

# Sort data points in each slice by y coordinate and create leaf nodes of 100 data points

Slice_1 = sorted(Slice_1 , key=lambda k: [k[1]])
Slice_2 = sorted(Slice_2 , key=lambda k: [k[1]])
Slice_3 = sorted(Slice_3 , key=lambda k: [k[1]])
Slice_4 = sorted(Slice_4 , key=lambda k: [k[1]])
Slice_5 = sorted(Slice_5 , key=lambda k: [k[1]])
Slice_6 = sorted(Slice_6 , key=lambda k: [k[1]])
Slice_7 = sorted(Slice_7 , key=lambda k: [k[1]])
Slice_8 = sorted(Slice_8 , key=lambda k: [k[1]])
Slice_9 = sorted(Slice_9 , key=lambda k: [k[1]])
Slice_10 = sorted(Slice_10 , key=lambda k: [k[1]])
Slice_11 = sorted(Slice_11 , key=lambda k: [k[1]])
Slice_12 = sorted(Slice_12 , key=lambda k: [k[1]])
Slice_13 = sorted(Slice_13 , key=lambda k: [k[1]])
Slice_14 = sorted(Slice_14 , key=lambda k: [k[1]])
Slice_15 = sorted(Slice_15 , key=lambda k: [k[1]])
Slice_16 = sorted(Slice_16 , key=lambda k: [k[1]])
Slice_17 = sorted(Slice_17 , key=lambda k: [k[1]])
Slice_18 = sorted(Slice_18 , key=lambda k: [k[1]])
Slice_19 = sorted(Slice_19 , key=lambda k: [k[1]])
Slice_20 = sorted(Slice_20 , key=lambda k: [k[1]])
Slice_21 = sorted(Slice_21 , key=lambda k: [k[1]])
Slice_22 = sorted(Slice_22 , key=lambda k: [k[1]])
Slice_23 = sorted(Slice_23 , key=lambda k: [k[1]])
Slice_24 = sorted(Slice_24 , key=lambda k: [k[1]])
Slice_25 = sorted(Slice_25 , key=lambda k: [k[1]])
Slice_26 = sorted(Slice_26 , key=lambda k: [k[1]])
Slice_27 = sorted(Slice_27 , key=lambda k: [k[1]])
Slice_28 = sorted(Slice_28 , key=lambda k: [k[1]])
Slice_29 = sorted(Slice_29 , key=lambda k: [k[1]])
Slice_30 = sorted(Slice_30 , key=lambda k: [k[1]])
Slice_31 = sorted(Slice_31 , key=lambda k: [k[1]])
Slice_32 = sorted(Slice_32 , key=lambda k: [k[1]])
Slice_33 = sorted(Slice_33 , key=lambda k: [k[1]])
Slice_34 = sorted(Slice_34 , key=lambda k: [k[1]])
Slice_35 = sorted(Slice_35 , key=lambda k: [k[1]])
Slice_36 = sorted(Slice_36 , key=lambda k: [k[1]])
Slice_37 = sorted(Slice_37 , key=lambda k: [k[1]])
Slice_38 = sorted(Slice_38 , key=lambda k: [k[1]])
Slice_39 = sorted(Slice_39 , key=lambda k: [k[1]])
Slice_40 = sorted(Slice_40 , key=lambda k: [k[1]])
Slice_41 = sorted(Slice_41 , key=lambda k: [k[1]])
Slice_42 = sorted(Slice_42 , key=lambda k: [k[1]])
Slice_43 = sorted(Slice_43 , key=lambda k: [k[1]])
Slice_44 = sorted(Slice_44 , key=lambda k: [k[1]])
Slice_45 = sorted(Slice_45 , key=lambda k: [k[1]])
Slice_46 = sorted(Slice_46 , key=lambda k: [k[1]])
Slice_47 = sorted(Slice_47 , key=lambda k: [k[1]])
Slice_48 = sorted(Slice_48 , key=lambda k: [k[1]])
Slice_49 = sorted(Slice_49 , key=lambda k: [k[1]])
Slice_50 = sorted(Slice_50 , key=lambda k: [k[1]])
Slice_51 = sorted(Slice_51 , key=lambda k: [k[1]])
Slice_52 = sorted(Slice_52 , key=lambda k: [k[1]])
Slice_53 = sorted(Slice_53 , key=lambda k: [k[1]])
Slice_54 = sorted(Slice_54 , key=lambda k: [k[1]])
Slice_55 = sorted(Slice_55 , key=lambda k: [k[1]])
Slice_56 = sorted(Slice_56 , key=lambda k: [k[1]])
Slice_57 = sorted(Slice_57 , key=lambda k: [k[1]])
Slice_58 = sorted(Slice_58 , key=lambda k: [k[1]])
Slice_59 = sorted(Slice_59 , key=lambda k: [k[1]])
Slice_60 = sorted(Slice_60 , key=lambda k: [k[1]])
Slice_61 = sorted(Slice_61 , key=lambda k: [k[1]])
Slice_62 = sorted(Slice_62 , key=lambda k: [k[1]])
Slice_63 = sorted(Slice_63 , key=lambda k: [k[1]])
Slice_64 = sorted(Slice_64 , key=lambda k: [k[1]])
Slice_65 = sorted(Slice_65 , key=lambda k: [k[1]])
Slice_66 = sorted(Slice_66 , key=lambda k: [k[1]])
Slice_67 = sorted(Slice_67 , key=lambda k: [k[1]])
Slice_68 = sorted(Slice_68 , key=lambda k: [k[1]])
Slice_69 = sorted(Slice_69 , key=lambda k: [k[1]])
Slice_70 = sorted(Slice_70 , key=lambda k: [k[1]])
Slice_71 = sorted(Slice_71 , key=lambda k: [k[1]])
Slice_72 = sorted(Slice_72 , key=lambda k: [k[1]])
Slice_73 = sorted(Slice_73 , key=lambda k: [k[1]])
Slice_74 = sorted(Slice_74 , key=lambda k: [k[1]])
Slice_75 = sorted(Slice_75 , key=lambda k: [k[1]])
Slice_76 = sorted(Slice_76 , key=lambda k: [k[1]])
Slice_77 = sorted(Slice_77 , key=lambda k: [k[1]])
Slice_78 = sorted(Slice_78 , key=lambda k: [k[1]])
Slice_79 = sorted(Slice_79 , key=lambda k: [k[1]])
Slice_80 = sorted(Slice_80 , key=lambda k: [k[1]])
Slice_81 = sorted(Slice_81 , key=lambda k: [k[1]])
Slice_82 = sorted(Slice_82 , key=lambda k: [k[1]])
Slice_83 = sorted(Slice_83 , key=lambda k: [k[1]])
Slice_84 = sorted(Slice_84 , key=lambda k: [k[1]])
Slice_85 = sorted(Slice_85 , key=lambda k: [k[1]])
Slice_86 = sorted(Slice_86 , key=lambda k: [k[1]])
Slice_87 = sorted(Slice_87 , key=lambda k: [k[1]])
Slice_88 = sorted(Slice_88 , key=lambda k: [k[1]])
Slice_89 = sorted(Slice_89 , key=lambda k: [k[1]])
Slice_90 = sorted(Slice_90 , key=lambda k: [k[1]])
Slice_91 = sorted(Slice_91 , key=lambda k: [k[1]])
Slice_92 = sorted(Slice_92 , key=lambda k: [k[1]])
Slice_93 = sorted(Slice_93 , key=lambda k: [k[1]])
Slice_94 = sorted(Slice_94 , key=lambda k: [k[1]])
Slice_95 = sorted(Slice_95 , key=lambda k: [k[1]])
Slice_96 = sorted(Slice_96 , key=lambda k: [k[1]])
Slice_97 = sorted(Slice_97 , key=lambda k: [k[1]])
Slice_98 = sorted(Slice_98 , key=lambda k: [k[1]])
Slice_99 = sorted(Slice_99 , key=lambda k: [k[1]])
Slice_100 = sorted(Slice_100 , key=lambda k: [k[1]])


Points = Slice_1
Points.extend(Slice_2)
Points.extend(Slice_3)
Points.extend(Slice_4)
Points.extend(Slice_5)
Points.extend(Slice_6)
Points.extend(Slice_7)
Points.extend(Slice_8)
Points.extend(Slice_9)
Points.extend(Slice_10)
Points.extend(Slice_11)
Points.extend(Slice_12)
Points.extend(Slice_13)
Points.extend(Slice_14)
Points.extend(Slice_15)
Points.extend(Slice_16)
Points.extend(Slice_17)
Points.extend(Slice_18)
Points.extend(Slice_19)
Points.extend(Slice_20)
Points.extend(Slice_21)
Points.extend(Slice_22)
Points.extend(Slice_23)
Points.extend(Slice_24)
Points.extend(Slice_25)
Points.extend(Slice_26)
Points.extend(Slice_27)
Points.extend(Slice_28)
Points.extend(Slice_29)
Points.extend(Slice_30)
Points.extend(Slice_31)
Points.extend(Slice_32)
Points.extend(Slice_33)
Points.extend(Slice_34)
Points.extend(Slice_35)
Points.extend(Slice_36)
Points.extend(Slice_37)
Points.extend(Slice_38)
Points.extend(Slice_39)
Points.extend(Slice_40)
Points.extend(Slice_41)
Points.extend(Slice_42)
Points.extend(Slice_43)
Points.extend(Slice_44)
Points.extend(Slice_45)
Points.extend(Slice_46)
Points.extend(Slice_47)
Points.extend(Slice_48)
Points.extend(Slice_49)
Points.extend(Slice_50)
Points.extend(Slice_51)
Points.extend(Slice_52)
Points.extend(Slice_53)
Points.extend(Slice_54)
Points.extend(Slice_55)
Points.extend(Slice_56)
Points.extend(Slice_57)
Points.extend(Slice_58)
Points.extend(Slice_59)
Points.extend(Slice_60)
Points.extend(Slice_61)
Points.extend(Slice_62)
Points.extend(Slice_63)
Points.extend(Slice_64)
Points.extend(Slice_65)
Points.extend(Slice_66)
Points.extend(Slice_67)
Points.extend(Slice_68)
Points.extend(Slice_69)
Points.extend(Slice_70)
Points.extend(Slice_71)
Points.extend(Slice_72)
Points.extend(Slice_73)
Points.extend(Slice_74)
Points.extend(Slice_75)
Points.extend(Slice_76)
Points.extend(Slice_77)
Points.extend(Slice_78)
Points.extend(Slice_79)
Points.extend(Slice_80)
Points.extend(Slice_81)
Points.extend(Slice_82)
Points.extend(Slice_83)
Points.extend(Slice_84)
Points.extend(Slice_85)
Points.extend(Slice_86)
Points.extend(Slice_87)
Points.extend(Slice_88)
Points.extend(Slice_89)
Points.extend(Slice_90)
Points.extend(Slice_91)
Points.extend(Slice_92)
Points.extend(Slice_93)
Points.extend(Slice_94)
Points.extend(Slice_95)
Points.extend(Slice_96)
Points.extend(Slice_97)
Points.extend(Slice_98)
Points.extend(Slice_99)
Points.extend(Slice_100)


#Creating leaf nodes
a = 0
i = 1
dict_leaf = {}
while i < 10001:
    dict_leaf[i] = Points[a:a+10]
    i+=1
    a+=10

with open("leaf_Nodes.csv", "w") as check :
    for p in dict_leaf:
        string = str(dict_leaf[p])
        string = string[1:len(string)-1]
        check.write("leaf" + str(p) + "," + string + "\n")

#Creating MBR for leaf nodes
a = 0
i = 1
dict_leaf_MBR = {}
while i < 10001:
    dict_leaf_MBR[i] =MBR(dict_leaf[i])
    i+=1

with open("leaf_MBR.csv", "w") as check :
    for p in dict_leaf_MBR:
        string = str(dict_leaf_MBR[p])
        string = string[1:len(string)-1]
        check.write("leaf_MBR_" + str(p) + "," + string + "\n")

#Storing values for creating MBR of level 2 child nodes
a = 0
i = 1
dict_level2_child = {}
while i < 1001:
    dict_level2_child[i] = Points[a:a+100]
    i+=1
    a+=100

#Creating MBR for level 2 child nodes
a = 0
i = 1
dict_level2_child_MBR = {}
while i < 1001:
    dict_level2_child_MBR[i] =MBR(dict_level2_child[i])
    i+=1

with open("level2_MBR.csv", "w") as check :
    for p in dict_level2_child_MBR:
        string = str(dict_level2_child_MBR[p])
        string = string[1:len(string)-1]
        check.write("level2_MBR_" + str(p) + "," + string + "\n")

#Storing values for creating MBR of level 1 child nodes
a = 0
i = 1
dict_level1_child = {}
while i < 101:
    dict_level1_child[i] = Points[a:a+1000]
    i+=1
    a+=1000
    
#Creating MBR for level 1 child nodes
a = 0
i = 1
dict_level1_child_MBR = {}
while i < 101:
    dict_level1_child_MBR[i] =MBR(dict_level1_child[i])
    i+=1

with open("level1_MBR.csv", "w") as check :
    for p in dict_level1_child_MBR:
        string = str(dict_level1_child_MBR[p])
        string = string[1:len(string)-1]
        check.write("level1_MBR_" + str(p) + "," + string + "\n")

 
#Storing values for creating MBR of root nodes
a = 0
i = 1
dict_root = {}
while i < 11:
    dict_root[i] = Points[a:a+10000]
    i+=1
    a+=10000

#Creating MBR for root nodes
a = 0
i = 1
dict_root_MBR = {}
while i < 11:
    dict_root_MBR[i] =MBR(dict_root[i])
    i+=1

with open("root_MBR.csv", "w") as check :
    for p in dict_root_MBR:
        string = str(dict_root_MBR[p])
        string = string[1:len(string)-1]
        check.write("root_MBR_" + str(p) + "," + string + "\n")

#Load range querys 
test_query = csv.reader(open("Test_Query.csv", "r"))
Range_Queries = []
for row in test_query:
    x1, x2, y1, y2 = row    
    Range_Queries.append((int(x1),int(x2),int(y1),int(y2)))

#Implement brute force range query algorithm
brute_force_answer = []
brute_start = time.time()

for range_query in Range_Queries:
    i = brute_force_range_query(range_query)
    brute_force_answer.append(i)
brute_end = time.time()
query_count = len(Range_Queries)
print("Start time for brute force algorithm",brute_start)
print("End time for brute force algorithm",brute_end)
print("The average time for",query_count,"queries to execute using brute force is :",(round((brute_end - brute_start),4)/query_count),"seconds")


#Implement r tree range query algorithm
r_tree_answer = []
tree_start = time.time()
for range_query in Range_Queries:
    i = r_tree_algorithm(range_query,dict_root_MBR,dict_level1_child_MBR,dict_level2_child_MBR,dict_leaf_MBR,dict_leaf)
    r_tree_answer.append(i)
tree_end = time.time()
query_count = len(Range_Queries)
print("Start time for r tree algorithm",tree_start)
print("End time for r tree force algorithm",tree_start)
print("The average time for",query_count,"queries to execute using r tree is :",(round((tree_end - tree_start),4)/query_count),"seconds")

# Display result
print("Brute force algorithm result is :")
print(brute_force_answer)
print("R tree algorithm result is :")
print(r_tree_answer)

#Store results in csv files    
with open("Brute_force_result.csv", "w") as check :
    count = 1
    while count <= query_count:
        check.write("Query "+str(count)+" has "+str(brute_force_answer[count-1])+" points\n")
        count += 1

with open("R_tree_result.csv", "w") as check :
    count = 1
    while count <= query_count:
        check.write("Query "+str(count)+" has "+str(r_tree_answer[count-1])+" points\n")
        count += 1





