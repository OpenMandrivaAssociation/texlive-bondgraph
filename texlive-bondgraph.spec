Name:		texlive-bondgraph
Version:	1.0
Release:	1
Summary:	Create bond graph figures in LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bondgraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bondgraph.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package draws bond graphs using PGF and TikZ.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
