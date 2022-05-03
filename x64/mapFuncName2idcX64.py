#  -*- coding:utf-8 -*-
import sys
import os


def map2idc(in_file, out_file):
    print("executing map2idc")
    with open(out_file, 'w') as fout:
        fout.write('#include <idc.idc>\n')
        fout.write('static main()\n{\n ')
        with open(in_file) as fin:
            filterName = input("filter the loc/sub/qword etc. reserved prefix filed?(Y/N)")
            filterArrarys=['sub_','loc_','byte_','qword_','off_','locret_','asc_','unk_',"_"]
            for line in fin:
                #print(line)
                list = line.split()
                if list and ":" in list[0]:
                    #print(list[0].split(":")[1])


                    if len(list) == 2 and str(list[0].split(":")[1]).isalnum():
                        flag=False
                        if filterName == 'Y':
                            for reserv in filterArrarys:

                                if list[1].startswith(reserv):
                                    flag=True
                                    break
                            if flag:
                                continue
                            print("imported "+list[1])
                            fout.write(' \tMakeName(0x%s, "%s");\n ' % (list[0].split(":")[1], list[1]))
                        elif filterName == 'N':
                            print("imported "+ list[1])
                            fout.write(' \tMakeName(0x%s, "%s");\n ' % (list[0].split(":")[1], list[1]))
                        else:
                            print("error options. exit...")
                            exit(1)
        fout.write('}\n ')


def main():
    print("main executing")
    from optparse import OptionParser
    parser = OptionParser(usage=' usage: %prog <map filename> ')
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.error(' incorrect number of arguments ')
    return map2idc(args[0], os.path.splitext(args[0])[0] + '.idc')


if __name__ == "__main__":
    print("starting")
    main()
    sys.exit()
