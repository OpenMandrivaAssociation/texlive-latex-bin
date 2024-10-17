Name:		texlive-latex-bin
Version:	71362
Release:	1
Summary:	LaTeX executables and man pages
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-tetex
Requires:	texlive-latex
Requires:	texlive-latex-bin.bin

%description
TeXLive latex-bin package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%_texmf_fmtutil_d/latex-bin
%doc %{_mandir}/man1/*
%doc %{_texmfdistdir}/doc/man/man1/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/latex-bin <<EOF
#
# from latex-bin:
latex pdftex language.dat -translate-file=cp227.tcx *latex.ini
pdflatex pdftex language.dat -translate-file=cp227.tcx *pdflatex.ini
dvilualatex luatex language.dat,language.dat.lua dvilualatex.ini
lualatex luatex language.dat,language.dat.lua lualatex.ini
#! luajitlatex luajittex language.dat,language.dat.lua lualatex.ini
EOF
