# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    target = x.to_s
    if target[0] == "-"
        return false
    elsif target == "0"
        return true    
    elsif target[-1] == "0"
        return false
    else
        if target.length % 2 == 0
            while target.length != 0 do
                if target[0] == target[-1]
                    target.slice!(0)
                    target.slice!(-1)
                else
                    return false
                end
            end
            return true
        else
           index = (target.length / 2)
           target.slice!(index)
           while target.length != 0 do
               if target[0] == target[-1]
                 target.slice!(0)
                 target.slice!(-1)
               else
                   return false
               end
           end
           return true
        end
    end               
end
