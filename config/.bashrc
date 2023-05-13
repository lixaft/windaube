# Bash configuration file.

# Disable MacOs warning on shell start.
export BASH_SILENCE_DEPRECATION_WARNING=1

# Enable colors.
export CLICOLOR=1

bind '"\eS":"cd $(python ~/.local/bin/stim-go | fzf)\n"'

# Define aliases.
alias docker="podman"
alias la="ls -al"
alias ll="ls -l"
alias refresh="source $HOME/.bashrc"
alias tree="tree -C"
alias vim="nvim"
alias e="Explorer"

# Extend $PATH.
export PATH+=":$HOME/.local/bin"
export PATH+=":$HOME/.cargo/bin"

# Python variables.
export PIP_DISABLE_PIP_VERSION_CHECK=1
export PYTHONSTARTUP="$HOME/.pythonrc"

# Initialize starship.
if [[ -x "$(command -v starship)" ]]; then
    eval "$(starship init bash)"
fi
