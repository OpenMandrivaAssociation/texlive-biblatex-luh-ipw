Name:		texlive-biblatex-luh-ipw
Version:	32180
Release:	2
Summary:	Biblatex styles for social sciences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-luh-ipw
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-luh-ipw.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-luh-ipw.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle is a small collection of styles for biblatex. It was
designed for citations in the Humanities, following the
guidelines of style of the institutes for the social sciences
of the Leibniz University Hannover/LUH (especially the
Institute of Political Science). The bundle depends on biblatex
(version 1.1 at least) and cannot be used without it.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/bbx/authoryear-luh-ipw.bbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/bbx/standard-luh-ipw.bbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/bbx/verbose-inote-luh-ipw.bbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/cbx/authoryear-luh-ipw.cbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/cbx/standard-luh-ipw.cbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/cbx/verbose-inote-luh-ipw.cbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/lbx/english-luh-ipw.lbx
%{_texmfdistdir}/tex/latex/biblatex-luh-ipw/lbx/german-luh-ipw.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-luh-ipw/README
%doc %{_texmfdistdir}/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-preamble.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-print.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-screen.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-luh-ipw/de-biblatex-luh-ipw.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-luh-ipw/de-biblatex-luh-ipw.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
