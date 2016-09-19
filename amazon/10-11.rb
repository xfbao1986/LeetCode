#!/usr/bin/ruby

a = gets().strip().to_i()

result = {}

if a == 0
    str = '0'

else

    while(a>0) do

        b = 0
        begin
            b += 1
        end while a >= 11**b
        b -= 1

        result[b] = a/11**b
        a = a - (result[b] * (11**b))

    end


    result = Hash[ result.sort.reverse ]

    str = ''
    i = result.keys().max()
    while i >= 0
        if result[i]

            str = result[i] == 10 ? str + 'a' : str + result[i].to_s
        else
            str = str + '0'
        end
        i -= 1
    end
end
print str
