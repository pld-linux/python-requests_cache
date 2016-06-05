# TODO
# - build and package docs
# - tests need redis and mongo db
#
# Conditional build:
%bcond_with	doc	# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	requests-cache
Summary:	Persistent cache for requests library
Name:		python-%{module}
Version:	0.4.6
Release:	0.1
License:	BSD
Source0:	https://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
Group:		Libraries/Python
URL:		https://github.com/reclosedev/requests-cache
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-requests >= 1.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-requests >= 1.1.0
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
BuildRequires:	python3-sphinx
%endif
Requires:	python-requests >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Requests-cache is a transparent persistent cache for the requests
library.

%package -n python3-%{module}
Summary:	Persistent cache for requests library
Group:		Libraries/Python
Requires:	python3-requests >= 1.1.0

%description -n python3-%{module}
Requests-cache is a transparent persistent cache for the requests
library.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py_sitescriptdir}/requests_cache
%{py_sitescriptdir}/requests_cache-%{version}*
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst LICENSE
%{py3_sitescriptdir}/requests_cache
%{py3_sitescriptdir}/requests_cache-%{version}*
%endif
