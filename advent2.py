# advent of code 2019 day 2

import csv

class Computer:
    def run(self, noun, verb):
        f = open('input2.txt', 'r')
        for line in f:
            program = line.split(',')
            program[1] = noun
            program[2] = verb
            i = 0
            while(program[i]!='99'):
                if program[i]=='1':
                    program[int(program[i+3])] = str(int(program[int(program[i+1])]) + int(program[int(program[i+2])]))
                if program[i]=='2':
                    program[int(program[i+3])] = str(int(program[int(program[i+1])]) * int(program[int(program[i+2])]))
                i = i + 4
            return program[0]


if __name__ == "__main__":
    comp = Computer()
    print(comp.run('12','2'))
    for i in range(99):
        for j in range(99):
            if comp.run(str(i),str(j)) == '19690720':
                print(100*i+j)

