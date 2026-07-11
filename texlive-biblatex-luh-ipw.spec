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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle is a small collection of styles for BibLaTeX. It was designed
for citations in the Humanities, following the guidelines of style of
the institutes for the social sciences of the Leibniz University
Hannover/LUH (especially the Institute of Political Science). The bundle
depends on BibLaTeX (version 1.1 at least) and cannot be used without
it.

