# revision 21670
# category Package
# catalog-ctan /macros/latex/contrib/bondgraph
# catalog-date 2011-03-09 21:09:16 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-bondgraph
Version:	1.0
Release:	2
Summary:	Create bond graph figures in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bondgraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraph.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 749799
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 717963
- texlive-bondgraph
- texlive-bondgraph
- texlive-bondgraph
- texlive-bondgraph
- texlive-bondgraph

