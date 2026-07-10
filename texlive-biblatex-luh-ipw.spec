%global tl_name biblatex-luh-ipw
%global tl_revision 32180

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	BibLaTeX styles for social sciences
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-luh-ipw
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-luh-ipw.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-luh-ipw.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle is a small collection of styles for BibLaTeX. It was designed
for citations in the Humanities, following the guidelines of style of
the institutes for the social sciences of the Leibniz University
Hannover/LUH (especially the Institute of Political Science). The bundle
depends on BibLaTeX (version 1.1 at least) and cannot be used without
it.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/bbx
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/cbx
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/lbx
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-preamble.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-print.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw/biblatex-luh-ipw-screen.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw/de-biblatex-luh-ipw.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-luh-ipw/de-biblatex-luh-ipw.tex
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/bbx/authoryear-luh-ipw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/bbx/standard-luh-ipw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/bbx/verbose-inote-luh-ipw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/cbx/authoryear-luh-ipw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/cbx/standard-luh-ipw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/cbx/verbose-inote-luh-ipw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/lbx/english-luh-ipw.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-luh-ipw/lbx/german-luh-ipw.lbx
