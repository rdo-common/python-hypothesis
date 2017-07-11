%global srcname hypothesis
%global sum A library for property based testing


Name:           python-%{srcname}
Version:        3.12.0
Release:        1%{?dist}
Summary:        %{sum}

License:        MPLv2.0
URL:            https://github.com/HypothesisWorks/hypothesis-python
Source0:        %{url}/archive/%{version}.tar.gz#/hypothesis-%{version}.tar.gz
# disable Sphinx extensions that require Internet access
Patch0:         %{srcname}-3.12.0-offline.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-sphinx
BuildRequires:  python-enum34
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%package     -n python2-%{srcname}
Summary:        A library for property based testing
Obsoletes:      python-%{srcname} < 1.11.1-1
Requires:       python-enum34

%{?python_provide:%python_provide python2-%{srcname}}
%if 0%{?fedora}
Suggests:       numpy
Suggests:       pytz
%endif

%description -n python2-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        A library for property based testing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
%if 0%{?fedora}
Suggests:       python%{python3_pkgversion}-numpy
Suggests:       python%{python3_pkgversion}-pytz
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Hypothesis is a library for testing your Python code against a much
larger range of examples than you would ever want to write by
hand. It’s based on the Haskell library, Quickcheck, and is designed
to integrate seamlessly into your existing Python unit testing work
flow.


%prep
%autosetup -n %{srcname}-python-%{version} -p1

# remove shebang, mergedbs gets installed in sitelib
%{__sed} -i -e 1,2d src/hypothesis/tools/mergedbs.py


%build
%py2_build
%py3_build
PYTHONPATH=src READTHEDOCS=True sphinx-build -b man docs docs/_build/man


%install
%py2_install
%py3_install
%{__install} -Dp -m 644 docs/_build/man/hypothesis.1 \
             $RPM_BUILD_ROOT%{_mandir}/man1/hypothesis.1


%files -n python2-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*
%{_mandir}/man1/hypothesis.1*

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
%{_mandir}/man1/hypothesis.1*


%changelog
* Mon Jul 10 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.12.0-1
- Update to 3.12.0
- Reenable docs in EPEL7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.4.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun May 29 2016 Michel Alexandre Salim <salimma@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Version the explicit Provides

* Wed May 04 2016 Nathaniel McCallum <npmccallum@redhat.com> - 3.1.3-1
- Update to 3.1.3
- Remove unused code
- Remove unused dependencies

* Sun Feb 14 2016 Michel Salim <salimma@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Sep 25 2015 Michel Salim <salimma@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Sun Sep 20 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Wed Sep  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-3
- Re-disable tests for now

* Tue Sep  1 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-2
- Disable Python3 tests - need debugging on ARM builders

* Mon Aug 31 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.6-1
- Update to 1.10.6
- Enable tests

* Fri Aug  7 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.10.0-1
- Update to 1.10

* Wed Jul 29 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.9.0-1
- Update to 1.9.0

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-2
- Remove she-bang from tools/mergedbs.py
- Include manpage

* Fri Jul 24 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.5-1
- Update to 1.8.5
- Make Python3 build unconditional

* Thu Jul 23 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8.2-1
- Initial package
