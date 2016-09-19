#!/usr/bin/ruby

num = gets().strip().to_i()
p num

param = {}
people = []
for i in 1..num do
    people.push i
    tmp = gets().strip().split(" ")
    param[i] = {}
    param[i]["l"] = tmp[0].to_i()
    param[i]["r"] = tmp[1].to_i()
    param[i]["k"] = tmp[2].to_i()
end

p param
p people

i = 1
people.delete(i)
l = param[i]["l"]
r = param[i]["r"]
min_k = nil

for j in l..r do

    t = j % people.size
    if min_k.nil?
        min_k = param[t]["k"]
    else
        min_k = min_k <= param[t]["k"] ? min_k : param[t]["k"]
    end

end
