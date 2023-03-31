Name:		texlive-glossaries-german
Version:	35665
Release:	2
Summary:	German language module for glossaries package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-german
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-german.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-german.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-german.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
German language module for the glossaries package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/glossaries-german
%{_texmfdistdir}/tex/latex/glossaries-german
%doc %{_texmfdistdir}/doc/latex/glossaries-german

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
