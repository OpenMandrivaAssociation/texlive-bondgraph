Name:		texlive-bondgraph
Version:	21670
Release:	1
Summary:	Create bond graph figures in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bondgraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraph.r21670.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraph.doc.r21670.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws bond graphs using PGF and TikZ.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bondgraph/bondgraph.sty
%doc %{_texmfdistdir}/doc/latex/bondgraph/License.txt
%doc %{_texmfdistdir}/doc/latex/bondgraph/README
%doc %{_texmfdistdir}/doc/latex/bondgraph/bondgraph_arrows.tex
%doc %{_texmfdistdir}/doc/latex/bondgraph/bondgraph_example.pdf
%doc %{_texmfdistdir}/doc/latex/bondgraph/bondgraph_example.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
