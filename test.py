#!/usr/bin/env python3
# -*- coding: utf-8 -*-

zero= ["  ***  ",
       " *   * ",
       "*     *",
       "*     *",
       "*     *",
       " *   * ",
       "  ***  " ]

one=  ["   *   ",
       "  **   ",
       " * *   ",
       "   *   ",
       "   *   ",
       "   *   ",
       "  ***  " ]

two=  ["  ***  ",
       " *   * ",
       " *   * ",
       "    *  ",
       "   *   ",
       "  *    ",
       " ***** " ]

three=["  ***  ",
       " *   * ",
       "    *  ",
       "   *   ",
       "    *  ",
       " *   * ",
       "  ***  " ]

four= ["    *  ",
       "   **  ",
       "  * *  ",
       " ****  ",
       "    *  ",
       "    *  ",
       "    *  " ]

five= [" ***** ",
       " *     ",
       " *     ",
       " ***** ",
       "     * ",
       "     * ",
       " ***** " ]

six=  [" ***** ",
       " *     ",
       " *     ",
       " ***** ",
       " *   * ",
       " *   * ",
       " ***** " ]

seven=[" ***** ",
       "     * ",
       "     * ",
       "    *  ",
       "   *   ",
       "  *    ",
       " *     " ]

eight=[" ***** ",
       " *   * ",
       " *   * ",
       " ***** ",
       " *   * ",
       " *   * ",
       " ***** " ]

nine= [" ***** ",
       " *   * ",
       " *   * ",
       " ***** ",
       "     * ",
       "     * ",
       " ***** " ]

digits = [zero,one,two,three,four,five,six,seven,eight,nine]

colon=["       ",
       "       ",
       "       ",
       "   *   ",
       "       ",
       "   *   ",
       "       " ]



from time import localtime as get_time

now = get_time()

h1 = 0 if now.tm_hour < 10 else 1
h2 = now.tm_hour - 10 if now.tm_hour >= 10 else now.tm_hour
m1 = int(now.tm_min / 10)
m2 = now.tm_min % 10


width = '=' * len(colon[0])
print( '{}'.format(width * 5) )

for i in range(len(colon)):
    print( '{}{}{}{}{}'.format(digits[h1][i],
                               digits[h2][i],
                               colon[i],
                               digits[m1][i],
                               digits[m2][i])) 

print( '{}'.format(width * 5) )
