import sys
import pprint

entities_list = ["p","i8","i16","i32","i64","f32","f64","v64","v128","a0","s0","f80","n8"]

test_string = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"

def parse_layout_s(layout_str = ""):
    types_d = {}
    res = {}
    tok1 = layout_str.split('-')
    res['order'] = {"Big Endian" if layout_str[0]=='E' else 'Little Endian', layout_str[0]}
    for t in tok1[1:-1]:
        token = t.split(":")
        types_d[token[0]] = token[1:]

    res['types'] = types_d
    return res


def layouts_diff(l1,l2):
    return


if __name__ == "__main__":
    if( len(sys.argv)<=1 or sys.argv[1]==(None or "-t" or "--test")):
        pprint.pprint(parse_layout_s(test_string))
    elif sys.argv[1]==("-p" or "--parse"):
        pprint.pprint(parse_layout_s(sys.argv[2]))
    elif sys.argv[1]==("-l" or "--ll"):
        with open(sys.argv[2]) as f:
            r=f.readline()
            pprint.pprint(parse_layout_s(r))
    elif len(sys.argv)==2:
        pprint.pprint(parse_layout_s(sys.argv[1]))
