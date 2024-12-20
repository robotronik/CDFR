# A python program to convert .obj files into arrays to copy paste into cpp files
# OBJ points are stored with format [i] = {x,y}
# OBJ lines are stored with format [k] = {i,j}

# Blender settings:
# - Export as Wavefront (.obj)
# - Selection Only
# - triangulate faces
# - Y Forward, Z Up
# - Dont write materials


import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python obj_to_highways.py <filename>")
        return

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("File not found")
        return

    obj_file = open(filename, "r")
    f_lines = obj_file.readlines()
    obj_file.close()

    points = []
    lines = []

    for f_line in f_lines:
        if f_line.startswith("v"):
            point = f_line.split()
            points.append((round(float(point[1])), round(float(point[2]))))
        elif f_line.startswith("l"):
            line = f_line.split()
            lines.append((int(line[1])-1, int(line[2])-1))
 
    print("#define HIGHWAY_POINTS_COUNT " + str(len(points)))
    print("#define HIGHWAY_LINES_COUNT " + str(len(lines)))
    
    print("static highway_point points[] = {", end="")
    for point in points:
        print("{" + str(point[0]) + ", " + str(point[1]) + "},", end="")
    print("};")
    print("static highway_line lines[] = {", end="")
    for line in lines:
        print("{" + str(line[0]) + ", " + str(line[1]) + "},", end="")
    print("};")

if __name__ == "__main__":
    main()