# GMScript

### This was made by [gnaboo](https://www.twitter.com/GabrielGnaboo)


## Documentation :

>Commands :

|Name|Type|Description|Arguments|Basic Command|
|----|----|-----------|---------|-------------|
|print|Debug|Prints out in console the arguments.| Int, String, Boolean, ***List, Dict***| Yes
|printf|Debug|Same as print but stays at the same line. |Int, String, Boolean, ***List, Dict***| Yes
|set|Variable|Creates and sets a variable to a value| Int, String, Boolean| Yes

> Arguments and Prefix : 

|Name|Type|Caracter|Use|Basic Command|
|-|-|-|-|-|
|Basic Prefix|Loop Indicator|`!`|To indicate that we are in the main loop| Yes
|Basic Argument|Argument Indicator|`$`|To indicate that what is after is an argument for the command| Yes
|Variable Argument| Argument Indicator|`%`|To indicate that what is in the variable is an argument for the command| Yes


## Exemples :

> Script :

```python
! print $First arg $Second arg
! set $ImAVariable:$Hey !
! print $%ImAVariable $Ho !
! printf $%ImAVariable
```
> Result :
```batch
First arg Second arg
Hey ! Ho !
Hey !
```

## How to Launch your script :

- For the moment, you can change the file which is being inspecting directly in the code...

