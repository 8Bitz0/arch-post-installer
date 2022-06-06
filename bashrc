#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Delete .bash_history
rm -f ~/.bash_history

alias ls='ls --color=auto'
alias cls='clear'

PS1='\e[36;1m\u\e[0m@\e[36;1m\h\e[0m \W> '

PATH='/home/alex/.local/bin':$PATH
