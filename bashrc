#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'

echo -e '         \e[1;36m.'
echo -e '        \e[1;36m/ \'
echo -e '       \e[1;36m/   \      \e[1;37m               #     \e[1;36m| *'
echo -e '      \e[1;36m/^.   \     \e[1;37m a##e #%" a#"e 6##%  \e[1;36m| | |-^-. |   | \ /'
echo -e '     \e[0;36m/  .-.  \    \e[1;37m.oOo# #   #    #  #  \e[1;36m| | |   | |   |  X'
echo -e '    \e[0;36m/  (   ) _\   \e[1;37m%OoO# #   %#e" #  #  \e[1;36m| | |   | ^._.| / \'
echo -e '   \e[0;36m/ _.~   ~._^\'
echo -e '  \e[0;36m/.^         ^.\'
echo -e ''

PS1='\e[36;1m\u\e[0m@\e[36;1m\h\e[0m \W> '