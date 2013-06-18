%global packname  EatonEtAlChIPseq
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.0.5
Release:          2
Summary:          ChIP-seq data of ORC-binding sites in Yeast excerpted from Eaton et al. 2010
Group:            Sciences/Mathematics
License:          Artistic 2.0
URL:              None
Source0:          http://bioconductor.org/packages/data/experiment/src/contrib/EatonEtAlChIPseq_0.0.5.tar.gz
BuildArch:        noarch
Requires:         R-core R-GenomicRanges R-ShortRead R-rtracklayer
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-GenomicRanges R-ShortRead R-rtracklayer

%description
ChIP-seq analysis subset from "Conserved nucleosome positioning defines
replication origins" (PMID 20351051)

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
