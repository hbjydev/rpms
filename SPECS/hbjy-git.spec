Name:     hbjy-git
Version:	1.0.0
Release:	1%{?dist}
Summary:	My personal Git scripts/aliases
License:	BSDv3

Requires: git

%description
This is a collection of my personal Git scripts & aliases, to improve my Git
workflow.

%prep
# No source included, no need for prep

%build
cat > aliases.sh <<EOF
#!/bin/bash
alias g='git' 2>/dev/null

alias ga='git add' 2>/dev/null
alias gaa='git add --all' 2>/dev/null

alias gb='git branch' 2>/dev/null

alias gc='git commit -v' 2>/dev/null
alias gcb='git checkout -b' 2>/dev/null
alias gcm='git checkout $(git_main_branch)' 2>/dev/null
alias gcd='git checkout develop' 2>/dev/null
alias gco='git checkout' 2>/dev/null
alias gcs='git commit -S' 2>/dev/null

alias gd='git diff' 2>/dev/null
alias gds='git diff --staged' 2>/dev/null

alias gs='git status' 2>/dev/null

alias gp='git push' 2>/dev/null

alias gup='git pull --rebase' 2>/dev/null
alias gupv='git pull --rebase -v' 2>/dev/null
alias gupa='git pull --rebase --autostash' 2>/dev/null
alias gupav='git pull --rebase --autostash -v' 2>/dev/null
alias glum='git pull upstream $(git_main_branch)' 2>/dev/null
EOF

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -Dm0755 aliases.sh %{buildroot}%{_sysconfdir}/profile.d/%{name}-aliases.sh
ls %{buildroot}%{_sysconfdir}/profile.d/

%files
%{_sysconfdir}/profile.d/%{name}-aliases.sh

%changelog
* Sat May 08 2021 Hayden Young <hi@hbjy.dev>
- Initial Package Release