import sys

entities_list = ["p","i8","i16","i32","i64","f32","f64","v64","v128","a0","s0","f80","n8"]

test_string = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"

def parse_layout_s(layout_str=""):
    types_d = {}
    res = []
    tok1 =layout_str.split('-')
    res.append(["Big Endian" if layout_str[0]=='E' else 'Little Endian', layout_str[0]])
    for token in tok1[1:-1]:
        #if not types_d.get(token[0]):
        #    print("")
        types_d[token[0]]=token[1:]
        
        print(token)
    return types_d

#def print_parsed_layout():


def layouts_diff(l1,l2):
    return

if __name__=="__main__":
    print(parse_layout_s(test_string))
