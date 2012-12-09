# revision 25093
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-luh-ipw
# catalog-date 2012-01-10 17:14:00 +0100
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-biblatex-luh-ipw
Version:	0.2
Release:	2
Summary:	Biblatex styles for social sciences
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-luh-ipw
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-luh-ipw.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-luh-ipw.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 770112
- Update to latest upstream package

* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 762532
- Update to latest upstream package

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 749608
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 729630
- texlive-biblatex-luh-ipw
- texlive-biblatex-luh-ipw

