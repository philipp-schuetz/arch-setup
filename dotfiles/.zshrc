# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
unsetopt autocd beep extendedglob nomatch notify
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/philipp/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

# Set Starship prompt
eval "$(starship init zsh)"

# Alias some commands
alias la='ls -A'
alias l='ls -CF'
alias ll='ls -alF'
alias ls='ls --color=auto'
alias mv='mv -i'
alias rm='rm -i'
alias cp='cp -i'
alias grep='grep --color=auto'
alias ..='cd ..'
alias vim='nvim'
alias grep='grep --color=auto'

# add apps to PATH
export PATH=/home/philipp/apps/pycharm-2023.2.1/bin:$PATH
export PATH=/home/philipp/apps/WebStorm-232.9921.42/bin:$PATH
export PATH=/home/philipp/apps:$PATH
