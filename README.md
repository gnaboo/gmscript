# gmscript
A script which should follow the instructions given in a .gm file. (Shi*ty Prefix-Based Programming Language)

> How does it work ?
gmscript is sort of a programming language. It's coded in python and prefix-based.
> Prefix-Based ? What does that even mean ?
Well, to be honest, i don't really know. Contrarilly to python which uses indents and java which used this thingys `{}`, gmscript has a default prefix, `!` which is used before every command. When entering a `if` loop per exemple, the prefix will need to be defined and you will use this prefix instead of the other one inside the `if` loop.
> Wow ? How does it look ?
```c++
! print $"hello"
! set "variable": $input $"what is your name"
! print $variable
! if $variable = $1: NewprefixLOL
NewprefixLOL print $"hello"
NewprefixLOL set $"variable2": $input $"what is your name"
! NewprefixLOL $end
! print $variable2
! print```
