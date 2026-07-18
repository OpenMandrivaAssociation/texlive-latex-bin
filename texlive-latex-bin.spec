%global tl_name latex-bin
%global tl_revision 78282
%global tl_bin_links dvilualatex:luatex latex:pdftex lualatex:luahbtex pdflatex:pdftex

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX executables and man pages
Group:		Publishing
URL:		https://www.ctan.org/pkg/latex-bin
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(amsmath)
Requires:	texlive(babel)
Requires:	texlive(cm)
Requires:	texlive(dehyph)
Requires:	texlive(firstaid)
Requires:	texlive(graphics)
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(l3backend)
Requires:	texlive(l3kernel)
Requires:	texlive(latex)
Requires:	texlive(latex-bin.bin)
Requires:	texlive(latex-fonts)
Requires:	texlive(latexconfig)
Requires:	texlive(lm)
Requires:	texlive(lua-uni-algos)
Requires:	texlive(luahbtex)
Requires:	texlive(luaotfload)
Requires:	texlive(luatex)
Requires:	texlive(pdftex)
Requires:	texlive(tex-ini-files)
Requires:	texlive(tools)
Requires:	texlive(unicode-data)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
LaTeX executables and man pages

