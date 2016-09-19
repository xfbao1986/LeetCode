#!/usr/bin/ruby

a = gets().strip()

a = a.split(" ")

words_num = a.size()
len = 0

a.each do |v|
    if v.include?('{') && v.include?('}') && !v.include?('.')
        v[0] =''
        v[-1]=''
        len += v.split(',').map!{|vv| vv.length}.max

    elsif v.include?('.')
        v[-1] = ''
        if v.include?('{') && v.include?('}')
            v[0] =''
            v[-1]=''
            len += v.split(',').map!{|vv| vv.length}.max
        else
            len += v.length
        end
    else
        len += v.length
    end
end

print (len.to_f/words_num)
