#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Delete .bash_history
rm -f ~/.bash_history

alias ls='ls --color=auto'
alias cls='clear'

echo 

PS1='\e[31;1m\u\e[0m@\e[31;2m\h\e[1m \W> '
