# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<!-- insertion marker -->
## [5.2.2](https://github.com/yaph/logya/releases/tag/5.2.2) - 2024-11-30

<small>[Compare with 5.2.1](https://github.com/yaph/logya/compare/5.2.1...5.2.2)</small>

### Fixed

- Fix logic to determine sort order in `_alpha_index()`. ([b468f32](https://github.com/yaph/logya/commit/b468f3263edc7a908b1dc5cc7f733828b58ef094) by Ramiro Gómez).

### Changed

- Changes. ([b3be03d](https://github.com/yaph/logya/commit/b3be03d1621871e8989d545c9c63ff180178e4b7) by Ramiro Gómez).

## [5.2.1](https://github.com/yaph/logya/releases/tag/5.2.1) - 2024-11-05

<small>[Compare with 5.2.0](https://github.com/yaph/logya/compare/5.2.0...5.2.1)</small>

## [5.2.0](https://github.com/yaph/logya/releases/tag/5.2.0) - 2024-11-05

<small>[Compare with 5.1.0](https://github.com/yaph/logya/compare/5.1.0...5.2.0)</small>

### Added

- Add pyproject.toml and update dependencies. Remove obsolote requirements and setup files. ([de0f5d7](https://github.com/yaph/logya/commit/de0f5d740f504e2198be1ebfe4af3525fb04ad1f) by Ramiro Gómez).
- Add CHANGELOG.md ([15a0205](https://github.com/yaph/logya/commit/15a0205c0f2e56d46115a32d37b9413bb03df781) by Ramiro Gómez).

### Fixed

- Fix linting issues. ([33962ca](https://github.com/yaph/logya/commit/33962ca244ab64edbdff512df0d687106f9b166d) by Ramiro Gómez).
- Fix typing issues ([df42711](https://github.com/yaph/logya/commit/df4271128d4e8eb1fa461103b716a6787b5e03d3) by Ramiro Gómez).
- Fix typo ([39c679a](https://github.com/yaph/logya/commit/39c679ae0c0505507ced84dd8251f36f42838654) by Ramiro Gómez).

### Removed

- Remove obsolete tasks ([52f00e9](https://github.com/yaph/logya/commit/52f00e9461d43891031a7ffbef32d8dab87bf9c5) by Ramiro Gómez).

## [5.1.0](https://github.com/yaph/logya/releases/tag/5.1.0) - 2023-12-23

<small>[Compare with 5.0.0](https://github.com/yaph/logya/compare/5.0.0...5.1.0)</small>

### Added

- Add make task to update packages and requirement files Upgrade packages ([ba28791](https://github.com/yaph/logya/commit/ba28791072357d2f0f5823b2b9a09baedd36219e) by Ramiro Gómez).

### Removed

- Remove link ([1aaf5b7](https://github.com/yaph/logya/commit/1aaf5b74bb0433f73611078c0dacb627d856ad34) by Ramiro Gómez).

## [5.0.0](https://github.com/yaph/logya/releases/tag/5.0.0) - 2022-01-24

<small>[Compare with 4.7.2](https://github.com/yaph/logya/compare/4.7.2...5.0.0)</small>

### Added

- Add pytest-cov requirement ([09bbaa4](https://github.com/yaph/logya/commit/09bbaa44cec8eb7f6147e7d15914370895098137) by Ramiro Gómez).
- Add github funding info ([6301e86](https://github.com/yaph/logya/commit/6301e86745a0c09f8706a05d1a01dcdc513a0e3f) by Ramiro Gómez).
- Add generator meta tag ([9a8c0ae](https://github.com/yaph/logya/commit/9a8c0aeb3c4a175148416c8384e0e183b72c299d) by Ramiro Gómez).
- Add and improve documentation Replace noindex with ignore. Remove credits section because links are broken. ([e58e9b0](https://github.com/yaph/logya/commit/e58e9b08045a7a62b6cb36466d64c31d7763c401) by Ramiro Gómez).
- Add cache decorator to util and use it for template._get_docs. ([cdf9efb](https://github.com/yaph/logya/commit/cdf9efb4cc3c21f9edc647f9eeef5cf090e69790) by Ramiro Gómez).
- Add tests and access Logya object as a fixture to avoid issues when all tests are run. ([b39e33f](https://github.com/yaph/logya/commit/b39e33fe199aaab4454fddc87b8bbf8bb0f79667) by Ramiro Gómez).
- Add TODO ([6839b4a](https://github.com/yaph/logya/commit/6839b4ab3c46663288cff15ec0224d8644bef319) by Ramiro Gómez).
- Add missing argument ([043e3fd](https://github.com/yaph/logya/commit/043e3fd06eb8efaad5cdecbb85484ae66a4bb477) by Ramiro Gómez).
- Add test_filesource_image ([e812f0d](https://github.com/yaph/logya/commit/e812f0d742b73ffb7e3b4c3d1474a7d71ababe0e) by Ramiro Gómez).
- Add header sections ([bfea187](https://github.com/yaph/logya/commit/bfea187c1c7efd677402c3db415296c9a2bd9117) by Ramiro Gómez).
- Add template attr ([9e8776e](https://github.com/yaph/logya/commit/9e8776eae8352da2747a603b01eb361a22ccf076) by Ramiro Gómez).
- Add test_filesource ([e7aaa89](https://github.com/yaph/logya/commit/e7aaa896092f60138f0fb01fd54d2b23939d1bfa) by Ramiro Gómez).
- Add test_get_docs ([e4204aa](https://github.com/yaph/logya/commit/e4204aaad1d196fca4d63d435fe1bf5aee0c25a7) by Ramiro Gómez).
- Add get_item function. ([120c427](https://github.com/yaph/logya/commit/120c4278b864a2fb9e4fee82e4a75230205d9c58) by Ramiro Gómez).
- Add filesource function. ([4573594](https://github.com/yaph/logya/commit/4573594c91ca40e1af6dfe2adc1453c7c4560779) by Ramiro Gómez).
- Add RSS feed to base site. Add links to menu. ([6ca2fe5](https://github.com/yaph/logya/commit/6ca2fe5be86b85ef9cdeb73bb20ed15454dec95b) by Ramiro Gómez).
- Add **kwargs to serve function ([d53281b](https://github.com/yaph/logya/commit/d53281b72aae87959433d1f73578d8c1e5e24a13) by Ramiro Gómez).
- Add alpha_index filter which works on a list of dicts. ([d9359fa](https://github.com/yaph/logya/commit/d9359fa99cb9361f554e9e25e4fee7f59f8c4add) by Ramiro Gómez).
- Add test_deduplicate and use pytest in coverage make task ([328ab13](https://github.com/yaph/logya/commit/328ab13fd9d36d2a897a1458baced772b898ac65) by Ramiro Gómez).
- Add test ([a274820](https://github.com/yaph/logya/commit/a2748204b70380eacfaf262ddc47e189ce1301e9) by Ramiro Gómez).
- Add tests for util module. Use punctuation, whitespace from string module as characters forbidden in URLs. ([720d611](https://github.com/yaph/logya/commit/720d6111cd93818aeb26859f0246cc0c22d1de0f) by Ramiro Gómez).
- Add attrs to document ([6c9aba6](https://github.com/yaph/logya/commit/6c9aba65ff1bc09490cebc30ec825ce0563b8a9c) by Ramiro Gómez).
- Add template_attrs function ([24bbdb1](https://github.com/yaph/logya/commit/24bbdb14e6745099cbdca841ea48f828124a379c) by Ramiro Gómez).
- Add read_content and update_collections methods to Logya class. ([2f798ee](https://github.com/yaph/logya/commit/2f798eef406baafa8c714a212e50c0b0d9a0b88e) by Ramiro Gómez).
- Add docstrings and type annotations. ([7d90988](https://github.com/yaph/logya/commit/7d909882833a015398be50e1f4040ff4641c8a34) by Ramiro Gómez).
- Add tests for content type and parse functions. Add test fixtures including a test for --- separator in doc attribute values and body. Remove obsolete tests. ([0fc7be0](https://github.com/yaph/logya/commit/0fc7be00f8b5225b3d0dac36d26eacbf4fd8224c) by Ramiro Gómez).
- Add _collection_index stub ([187747d](https://github.com/yaph/logya/commit/187747ddf5ca3d3c314c04785c418d2c7deca20e) by Ramiro Gómez).
- Add deduplicate function ([7e2a2d8](https://github.com/yaph/logya/commit/7e2a2d8229fd284f0a099d95686ce9245b168775) by Ramiro Gómez).
- Add type annotations and remove comments ([b9b7010](https://github.com/yaph/logya/commit/b9b70101cfb87275bf4e92c9722b9e636222af40) by Ramiro Gómez).
- Add test_create_url ([a185f4e](https://github.com/yaph/logya/commit/a185f4e3602de3762b226f07133451c461699739) by Ramiro Gómez).
- Add break so else is not executed when doc was updated ([afffe64](https://github.com/yaph/logya/commit/afffe640853298386862803486465ec6d808ea9e) by Ramiro Gómez).
- Add and use collection_links macro ([ea9b4c8](https://github.com/yaph/logya/commit/ea9b4c832152752ff2f8702023d4a200377418a3) by Ramiro Gómez).
- Add base site files ([4ea2c20](https://github.com/yaph/logya/commit/4ea2c20887a8aad4caab07f14e36d35594afebc3) by Ramiro Gómez).
- Add paths argument to read_* functions. ([09046dc](https://github.com/yaph/logya/commit/09046dc7745c7fb85a69d71e1533d637d4dd98c1) by Ramiro Gómez).
- Add encode_content function from writer module. ([20f691c](https://github.com/yaph/logya/commit/20f691c1407ed02a6be5a55d62ee9f96d38a0ba6) by Ramiro Gómez).
- Add TODO section ([1355b22](https://github.com/yaph/logya/commit/1355b2282ae75636e1354da92eb565bdb0e8c0e2) by Ramiro Gómez).
- Add class variable L to HTTPRequestHandler to access Logya instance inside methods. ([020f7b4](https://github.com/yaph/logya/commit/020f7b48a1375f3b8b1d966dab12e6db15128ce2) by Ramiro Gómez).
- Add ipython and ipdb ([8426215](https://github.com/yaph/logya/commit/8426215209f07461d6288523e0aaae835a6e9a0f) by Ramiro Gómez).
- Add simpler template2 module and use it in content. ([fc7a46b](https://github.com/yaph/logya/commit/fc7a46b7165bff7e2e206b719ed7d2b251cd24ab) by Ramiro Gómez).
- Add option short names. ([c8491b7](https://github.com/yaph/logya/commit/c8491b71ea22b7a6cc1b09266a64eb1f49ac7310) by Ramiro Gómez).
- Add path_dst to write_page and call it from server.py ([7ae5247](https://github.com/yaph/logya/commit/7ae52474a2c6328bd82a9e1f4199effd2962198d) by Ramiro Gómez).
- Add FIXME ([aab2097](https://github.com/yaph/logya/commit/aab2097ba04fe19ad3b24aa47b3dff6f8675999c) by Ramiro Gómez).
- Add watchgod event handler stubs ([3a6a644](https://github.com/yaph/logya/commit/3a6a644dca23fb6c80384c7b6a7bd123928b736e) by Ramiro Gómez).
- Add doc string ([91f4206](https://github.com/yaph/logya/commit/91f4206d9b1045858f69212fb426a7aa4c3a1483) by Ramiro Gómez).
- Add url and collection links in read function. Add paths and config to util and use them. ([f8889a7](https://github.com/yaph/logya/commit/f8889a7a18f8ad9a63f75b36972012f0c0e3664e) by Ramiro Gómez).
- Add and call add_collections that adds document collections to the site index. ([e5002ba](https://github.com/yaph/logya/commit/e5002ba54d6fcdd45dff71de2becb4dc9c98421d) by Ramiro Gómez).
- Add content.py and test_content.py. Port test_docparser.py to pytest. Use pytest for running tests. ([309214a](https://github.com/yaph/logya/commit/309214a83a3197fa53b0500ab4a8b9a3b55c83ff) by Ramiro Gómez).
- Add build_all flag in serve mode to speed up serving by default. ([b9fbf5b](https://github.com/yaph/logya/commit/b9fbf5b44182228bffa770507d290f0dc4b2194e) by Ramiro Gómez).
- Add build_index argument. ([8d92b9c](https://github.com/yaph/logya/commit/8d92b9c471d8a023056bdce8653196c352c42439) by Ramiro Gómez).

### Fixed

- Fix jinja2 deprecations ([d299201](https://github.com/yaph/logya/commit/d299201f6bcd1554d91375203932b6c3d6cb6332) by Ramiro Gómez).
- Fix #87: Add sep=' ', timespec='seconds' arguments to isoformat calls in encoder.py ([9647f58](https://github.com/yaph/logya/commit/9647f58a0b8653b56ad64332e235a76cab3acda9) by Ramiro Gómez).
- Fix test image name ([7b0934d](https://github.com/yaph/logya/commit/7b0934d2dd5a21b877c15b956c12c62ddfc8a301) by Ramiro Gómez).
- Fix merge conflicts Remove sphinx docs ([fe93603](https://github.com/yaph/logya/commit/fe93603e0897c2c95b7c0553b684186c30f26b6e) by Ramiro Gómez).
- Fix docs. ([e31c9b7](https://github.com/yaph/logya/commit/e31c9b7c83e461eda09392b578e342348d30c356) by Ramiro Gómez).
- Fix more typing errors. ([9c98748](https://github.com/yaph/logya/commit/9c98748c54e0bdd60226f3538e2287ea2c622973) by Ramiro Gómez).
- Fix typing errors ([eee665d](https://github.com/yaph/logya/commit/eee665d24fd03b6929c375c917a2152f7f6046d8) by Ramiro Gómez).
- Fix variable names ([992ad71](https://github.com/yaph/logya/commit/992ad71c75f089d2b8281c4b82449b0dcab51cd8) by Ramiro Gómez).
- Fix syntax error ([46858c3](https://github.com/yaph/logya/commit/46858c3d8c0e0cbb38c2cd96cc19f0fcaf48baa4) by Ramiro Gómez).
- Fix import ([e101dd0](https://github.com/yaph/logya/commit/e101dd0a2e5f288049ec30cab291358dfe28523e) by Ramiro Gómez).
- Fix function calls. Move deploy to public. ([8a5dcbf](https://github.com/yaph/logya/commit/8a5dcbf13a4ff5a7f3d589bee3c81f64b1c0889a) by Ramiro Gómez).
- Fix index_url and canonical. ([41f0dec](https://github.com/yaph/logya/commit/41f0decbe7358f5eacd379d80b804bdc044bcb4e) by Ramiro Gómez).

### Changed

- Change error message. Add write_page function. ([505c3be](https://github.com/yaph/logya/commit/505c3beb5ffe4e2fb560b2ff5733bd10c1d510c2) by Ramiro Gómez).
- Change 2nd read parameter. ([182982f](https://github.com/yaph/logya/commit/182982f5a26caac3a92a7fad254c9f2d1df25770) by Ramiro Gómez).

### Removed

- Remove obsolete make tasks Use the new logo for all sites Make i18n site work ([a9f256a](https://github.com/yaph/logya/commit/a9f256ac8840e21b348ac842b35683224e25b613) by Ramiro Gómez).
- Remove site_index.py script from base site Use base_url and fix changes pages in docs site ([699b209](https://github.com/yaph/logya/commit/699b2090cb90954da9ddda499b95269edf146eb6) by Ramiro Gómez).
- Remove unused deduplicate and get_item functions. Add template tests. ([9cc196c](https://github.com/yaph/logya/commit/9cc196c3f1a7a634cc6cc42b8e4422bd0f4cd1c8) by Ramiro Gómez).
- Remove done tasks and ideas I won't implement ([429da24](https://github.com/yaph/logya/commit/429da2426e4e2897b759b2056bb8edbdb36a840c) by Ramiro Gómez).
- Remove write_doc function. Type annotations and mypy fixes. ([7b74a1b](https://github.com/yaph/logya/commit/7b74a1bb4ab70af8f17a97bc8ed03671eee2b419) by Ramiro Gómez).
- Remove obsolete function arguments. ([ea12567](https://github.com/yaph/logya/commit/ea1256735955e1bf777fe23a93ff64a8db76d34c) by Ramiro Gómez).
- Remove settings argument from write_collections. ([a0d82cb](https://github.com/yaph/logya/commit/a0d82cb43a0c05a626b66f825d6818b35b57e480) by Ramiro Gómez).
- Remove template_attrs function ([e49de92](https://github.com/yaph/logya/commit/e49de9201328c10a1b9aa63763e339a2f796e9ce) by Ramiro Gómez).
- Remove front.html template ([2b43b75](https://github.com/yaph/logya/commit/2b43b7568541db9342b76031c841cb7de433d389) by Ramiro Gómez).
- Remove _content_list function ([219b54f](https://github.com/yaph/logya/commit/219b54fb17fb7537c1a0239726c2e880e3f186f6) by Ramiro Gómez).
- Remove unused import ([bf65a5d](https://github.com/yaph/logya/commit/bf65a5d5690094278f360203b606bbd128ebdc7b) by Ramiro Gómez).
- Remove unused get_collection_name function. Mark functions that are not called in library. Simplify _get_docs. ([7db1f63](https://github.com/yaph/logya/commit/7db1f63959b27ebe2a1cf00885f34da5ad443308) by Ramiro Gómez).
- Remove collection_index global. ([aa41433](https://github.com/yaph/logya/commit/aa4143306080513a474dc9ec109de79e04341c81) by Ramiro Gómez).
- Remove old tests ([bc2dc76](https://github.com/yaph/logya/commit/bc2dc763710924ebfd67ba8eec7856fef2ed79f5) by Ramiro Gómez).
- Remove done tasks ([4b70695](https://github.com/yaph/logya/commit/4b70695beb669aaf05d29e628afc8c504a871c9b) by Ramiro Gómez).
- remove newline ([ae2dd4a](https://github.com/yaph/logya/commit/ae2dd4a9051be9e39242c247de5905eb541d754e) by Ramiro Gómez).
- Remove starter site ([0caf8e8](https://github.com/yaph/logya/commit/0caf8e8047fa48cff9919a9bbbade8400a749bec) by Ramiro Gómez).
- Remove temporary ignores ([8a55cf9](https://github.com/yaph/logya/commit/8a55cf9edb7954b7b32286dc6d79e7f6059e5a3e) by Ramiro Gómez).
- Remove docparser and docreader modules. ([7914ca2](https://github.com/yaph/logya/commit/7914ca2ec2f49742b0814f3ede7f587d58fb60e2) by Ramiro Gómez).
- Removed config module. ([894f2f1](https://github.com/yaph/logya/commit/894f2f12b94fa8b7b1c74546a13a95f51912b4a7) by Ramiro Gómez).
- Remove flatten_content.py and profile_generate.py scripts. ([3ade659](https://github.com/yaph/logya/commit/3ade65904c3a26eafacf50b6bae72906005e00d8) by Ramiro Gómez).
- Remove unused modules: path, serve and writer. ([3029d1a](https://github.com/yaph/logya/commit/3029d1a7b364ff4bf68c1e27e944ac253e8fc690) by Ramiro Gómez).
- Remove all methods in core not in use in v5. ([3a4ed41](https://github.com/yaph/logya/commit/3a4ed415424bb7c57006bd4920b039311c46ddff) by Ramiro Gómez).
- Remove init_env method ([5fa413a](https://github.com/yaph/logya/commit/5fa413aa07bccae14524a50b2139ae05a9ac3597) by Ramiro Gómez).
- Remove obsolete logic ([d5be6f8](https://github.com/yaph/logya/commit/d5be6f897416dcd82cbc6c46b8225d8c3f1b7491) by Ramiro Gómez).
- Remove newlines ([848d244](https://github.com/yaph/logya/commit/848d24465ce77c89de5079d471f87deefb99769e) by Ramiro Gómez).
- Remove unused import. Added FIXME ([e48980a](https://github.com/yaph/logya/commit/e48980a817181992ae32d8af694b57bf777bcb58) by Ramiro Gómez).
- Remove merge conflict ([a100bb0](https://github.com/yaph/logya/commit/a100bb0035ba303753429875842f0e2197690969) by Ramiro Gómez).
- Remove not existing import ([00e42da](https://github.com/yaph/logya/commit/00e42da665ac25e9d793f331adf4ce58c5bd67b9) by Ramiro Gómez).
- Remove watchgod and multiprocessing code ([7e6226a](https://github.com/yaph/logya/commit/7e6226a5e8d755cf5cda2b409af0a061677da357) by Ramiro Gómez).
- Remove print ([6de2075](https://github.com/yaph/logya/commit/6de20758383869972c96252a52005c2eac939d94) by Ramiro Gómez).
- Remove obsolete serve.py ([066615b](https://github.com/yaph/logya/commit/066615bdc24020e83952cffd76974d3ea7f65659) by Ramiro Gómez).

## [4.7.2](https://github.com/yaph/logya/releases/tag/4.7.2) - 2020-11-18

<small>[Compare with 4.7.1](https://github.com/yaph/logya/compare/4.7.1...4.7.2)</small>

### Added

- Add .nojekyll file to static dirs to avoid file name issues when using GitHub pages ([1e7adcf](https://github.com/yaph/logya/commit/1e7adcf7dc4bbcd3a4abd3e77f9ef382715617cf) by Ramiro Gómez).

## [4.7.1](https://github.com/yaph/logya/releases/tag/4.7.1) - 2020-02-18

<small>[Compare with 4.7.0](https://github.com/yaph/logya/compare/4.7.0...4.7.1)</small>

### Fixed

- Fix file name ([d1a4b45](https://github.com/yaph/logya/commit/d1a4b45e1addbb210820a467a9d945b8282d8339) by Ramiro Gómez).

## [4.7.0](https://github.com/yaph/logya/releases/tag/4.7.0) - 2020-01-20

<small>[Compare with 4.6.0](https://github.com/yaph/logya/compare/4.6.0...4.7.0)</small>

### Added

- Add info about last 4.x release with new features. Simplify changelog headings. ([6a21040](https://github.com/yaph/logya/commit/6a210408bcf9393758c627ff2fa62f5065fe63f8) by Ramiro Gómez).
- Add script for profiling the generate process. ([73111cf](https://github.com/yaph/logya/commit/73111cf0f1ab101ad0c75ab23de6e121a8eb656f) by Ramiro Gómez).
- Add funding file ([ed234cd](https://github.com/yaph/logya/commit/ed234cd5ed46c6d1400ffe1a7df7ecf78d4a8de9) by Ramiro Gómez).
- Add sites built with Logya ([caef6ef](https://github.com/yaph/logya/commit/caef6ef61599a523f976f480a1ee591ec024260d) by Ramiro Gómez).
- Add argcomplete requirement ([c222657](https://github.com/yaph/logya/commit/c222657b37e8566760a0ba0e943379f0c44de0c3) by Ramiro Gómez).
- Add command completion to getting started ([0039af0](https://github.com/yaph/logya/commit/0039af0b870101d2b6d86f66ab0a9701d7444e38) by Ramiro Gómez).

### Fixed

- Fix issue #90: Add collection_index function in template.py. ([f104130](https://github.com/yaph/logya/commit/f1041305fdf9d2b2ee84ca07ed5e9e94f0f321e7) by Ramiro Gómez).
- Fix issue #89: Rename alpha_index to doc_index. ([f0a8f60](https://github.com/yaph/logya/commit/f0a8f6029dfd40a49047095161341dfee627a945) by Ramiro Gómez).
- Fix issue #84: remove argcomplete. ([2f532f6](https://github.com/yaph/logya/commit/2f532f6f7d8b73e100c246fb2579833e767d4826) by Ramiro Gómez).

### Removed

- Remove newline ([41a3356](https://github.com/yaph/logya/commit/41a335666dd741badaad8f553a905e3199b38b62) by Ramiro Gómez).
- Remove disfunct landscape service ([de25d4a](https://github.com/yaph/logya/commit/de25d4ae22f92ced152dfe44e096407830d27e2e) by Ramiro Gómez).
- Remove binary dump ([dba6331](https://github.com/yaph/logya/commit/dba6331aa407a72a4f7c41d53765b1023da80154) by Ramiro Gómez).

## [4.6.0](https://github.com/yaph/logya/releases/tag/4.6.0) - 2019-08-15

<small>[Compare with 4.4.0](https://github.com/yaph/logya/compare/4.4.0...4.6.0)</small>

### Added

- Add script that creates markdown versions of content files and flattens the content directory structure. ([f3e8ffc](https://github.com/yaph/logya/commit/f3e8ffce89fe13dc46ba5f3823a1ef73d727c6f0) by Ramiro Gómez).
- Add support for multi-lingual indexes and add sample i18n site. ([3c1bcd6](https://github.com/yaph/logya/commit/3c1bcd6e9861890db192fc0f300a01e0f6b220f7) by Ramiro Gómez).

### Fixed

- Fix typos ([fbd87b2](https://github.com/yaph/logya/commit/fbd87b239618ea5df5c3da52fdfdd32bacfbe2a7) by Ramiro Gómez).

### Removed

- Remove support for Python 3.4 as latest Markdown requires at least Python 3.5. Bump Logya version to 4.5.0 ([943f292](https://github.com/yaph/logya/commit/943f292dc71fd30c43ae0de8d7ff2dcc879eecea) by Ramiro Gómez).
- Remove language prefix from index path when determining the template to use. ([2a6e021](https://github.com/yaph/logya/commit/2a6e02156ec41f3078cddce2c231a97482d5b293) by Ramiro Gómez).

## [4.4.0](https://github.com/yaph/logya/releases/tag/4.4.0) - 2019-02-05

<small>[Compare with 4.3.0](https://github.com/yaph/logya/compare/4.3.0...4.4.0)</small>

### Added

- Add info to changelog ([a106242](https://github.com/yaph/logya/commit/a106242daed77b5a210edfe3ab19cb97e0e0088b) by Ramiro Gómez).
- Add changelog item ([64e6743](https://github.com/yaph/logya/commit/64e6743185306260466239ceb1742f0df4b8285b) by Ramiro Gómez).
- Add build and write function to make it easy to subclass Generate and overwrite build step ([8beb6dd](https://github.com/yaph/logya/commit/8beb6ddd2e58d6a3e54ab297d490c6650fb85a9d) by Ramiro Gómez).

### Removed

- Remove Python 3.3 from travis config wheel needed for release task ([cabaf3e](https://github.com/yaph/logya/commit/cabaf3e7dba77e376b913c2440f2c313b2b92270) by Ramiro Gómez).

## [4.3.0](https://github.com/yaph/logya/releases/tag/4.3.0) - 2018-12-01

<small>[Compare with 4.2.0](https://github.com/yaph/logya/compare/4.2.0...4.3.0)</small>

### Added

- Add ``--site`` option to choose the base site to use when creating a new one. Add ``bare`` base site with minimal markup and files. Document site option in new create section together with directory layout Remove example site.yaml from docs Update pypi packages Update version to 4.3.0 ([8eb50fe](https://github.com/yaph/logya/commit/8eb50fe42c4938d4c2a2318e77a53ce2bf6b6ec6) by Ramiro Gómez).
- Add recipe Add requirement ([92a2912](https://github.com/yaph/logya/commit/92a2912eb0161765bd8e77e8500b1fbe86a8bfd4) by Ramiro Gómez).

### Removed

- Remove obsolete configuration Add newer Python versions Change tox config to use py36 ([488c3d8](https://github.com/yaph/logya/commit/488c3d8bef6e86f058d40df8591511a03eb9eded) by Ramiro Gómez).
- Remove obsolete make task ([34f8e4f](https://github.com/yaph/logya/commit/34f8e4f8ad5090e6ab1aaec140a3062e952dd329) by Ramiro Gómez).

## [4.2.0](https://github.com/yaph/logya/releases/tag/4.2.0) - 2018-05-27

<small>[Compare with 4.1.0](https://github.com/yaph/logya/compare/4.1.0...4.2.0)</small>

### Added

- Add attr_contains template filter to enable filtering docs with an attribute containing a given value. ([d5a8501](https://github.com/yaph/logya/commit/d5a8501bd19b0db78e9ed913df4d006e081d342b) by Ramiro Gómez).
- Add git tag to release task Update docs ([48d5a23](https://github.com/yaph/logya/commit/48d5a2366cfb8cf670308de8a18bb740fb68caa9) by Ramiro Gómez).

### Changed

- Change to https URLs ([9c4e01c](https://github.com/yaph/logya/commit/9c4e01c2c7cd3b93c3d9396ecaece5ee3f9a2564) by Ramiro Gómez).
- Change example site URL ([910cc77](https://github.com/yaph/logya/commit/910cc77bbf01ce163d872575216ec62fb82c275f) by Ramiro Gómez).

## [4.1.0](https://github.com/yaph/logya/releases/tag/4.1.0) - 2017-08-08

<small>[Compare with 4.0.0](https://github.com/yaph/logya/compare/4.0.0...4.1.0)</small>

### Added

- Add raw keyword argument to filesource function, which defaults to False. Update Python packages. ([b9900aa](https://github.com/yaph/logya/commit/b9900aa7a13698147384f96fbbbcbd31c34976d6) by Ramiro Gómez).
- added keep option for generate command started implementing rsync to use when keep is enabled ([3783a3d](https://github.com/yaph/logya/commit/3783a3d639264316632cf2dbd022e7363e4172bb) by Ramiro Gómez).
- Added get_index_template method to core. Don't allow for duplicate docs in collections. Added parent_paths to path module. More meaningful test variable names. ([9805d54](https://github.com/yaph/logya/commit/9805d54b3ae0d0437c2af4515ecd90299d5921f9) by Ramiro Gómez).
- added bugfix to changelog ([1807c84](https://github.com/yaph/logya/commit/1807c84d2f627b7fc04bcb066669fb6583bb83e0) by Ramiro Gómez).

### Removed

- removed .well-known rewrites from htaccess ([356c3a6](https://github.com/yaph/logya/commit/356c3a66e05f7c05626c96afce3415a957d02a36) by Ramiro Gómez).

## [4.0.0](https://github.com/yaph/logya/releases/tag/4.0.0) - 2016-08-07

<small>[Compare with first commit](https://github.com/yaph/logya/compare/237aa30ecb877611453ac6b098c6b307b25a4c22...4.0.0)</small>

### Added

- Added encode_content function. ([c352a0a](https://github.com/yaph/logya/commit/c352a0adf9582366400ff09c20bd676348f23613) by Ramiro Gómez).
- Added recommended packages to install docs. ([8643dbd](https://github.com/yaph/logya/commit/8643dbd6579b28086f65fd2779c993410fcd43c4) by Ramiro Gómez).
- Added write_content function. ([6e5cc41](https://github.com/yaph/logya/commit/6e5cc4147053c2e7eeab88ba07adeb9121d3b20d) by Ramiro Gómez).
- Added clean-starter-site task ([4852433](https://github.com/yaph/logya/commit/48524332cd8f319b9b6a7a9781fbab16b3c16c4e) by Ramiro Gómez).
- added classifiers ([4f6b4f4](https://github.com/yaph/logya/commit/4f6b4f45bd67474e00961fceae8ef324908dd121) by Ramiro Gómez).
- Added dev requirements and generated docs files ([5a69798](https://github.com/yaph/logya/commit/5a697981e944b2c540602f5980ab790e977f233d) by Ramiro Gómez).
- Added Contributing docs and Makefile. Updated required python libs. Use tox for running tests against different python versions. ([0b37839](https://github.com/yaph/logya/commit/0b37839a66589303445eac73d346d996ba914c22) by Ramiro Gómez).
- Added path module and tests for it Moved logya.get_path to path.join. ([d9d35d5](https://github.com/yaph/logya/commit/d9d35d5b2d376d89dbfe6b1d75a8b52c2569b415) by Ramiro Gómez).
- added sample logya site ([ea04648](https://github.com/yaph/logya/commit/ea046483730a9d8a68492340da0c3aa7da8630dc) by Ramiro Gómez).
- added test for docreader.markup_type ([54ddf46](https://github.com/yaph/logya/commit/54ddf463054a0c0bfb4e172a286e7d777bdfff22) by Ramiro Gómez).
- added docparser test ([34995f2](https://github.com/yaph/logya/commit/34995f27da953b4b9ee03d8cd3545f6c3e6bba17) by Ramiro Gómez).
- added default robots.txt ([072d461](https://github.com/yaph/logya/commit/072d461752bda33b25c7846a32eb960804859f3f) by Ramiro Gómez).
- Added Article markup to post template ([4c18b13](https://github.com/yaph/logya/commit/4c18b136099694f7a2a3ce56a276f8edbd973f5b) by Ramiro Gómez).
- Added datePublished and dateUpdated schema markup to postinfo. ([85c04ed](https://github.com/yaph/logya/commit/85c04ed65fe7ffba5d1f599f0d2a452409cb4da4) by Ramiro Gómez).
- Added postinfo template and sample post that displays it. Added author setting to site.yaml. ([244fa8e](https://github.com/yaph/logya/commit/244fa8e2e34631ce052485f6989230e6780f1697) by Ramiro Gómez).
- added doc_link macro ([f8eaaca](https://github.com/yaph/logya/commit/f8eaacae94d7898fc2b056fec2472e2e13a79ce8) by Ramiro Gómez).
- added get_docs template global that allows getting a document object in a template via the URL ([1bf1318](https://github.com/yaph/logya/commit/1bf13181af5e54c7133d9de75ac6ed540ba6add0) by Ramiro Gómez).
- added starter site readme ([5931ca2](https://github.com/yaph/logya/commit/5931ca2239e992e845ea74e257f0f255a385cad1) by Ramiro Gómez).
- added landscape config: ignore docs dir ([7e24daa](https://github.com/yaph/logya/commit/7e24daa3e1e103bdfda2cbddc9ff96cc4c033367) by Ramiro Gómez).
- added landscape badge ([5b2d3a7](https://github.com/yaph/logya/commit/5b2d3a7099766b6a3eaea246527940f3d9a3fd49) by Ramiro Gómez).
- added logya powered site ([0fd8cec](https://github.com/yaph/logya/commit/0fd8cec28f065fb19d49e041e9c37acbb8d02434) by Ramiro Gómez).
- added optional lines parameter to filesource function added inline docs for filesource ([ef2fa1f](https://github.com/yaph/logya/commit/ef2fa1fe1916bdfd1582c6975591a5a9a7b0d2f9) by Ramiro Gómez).
- added sites built with logya ([9043af0](https://github.com/yaph/logya/commit/9043af0c05c11a8d1b596baf149051df3cca36d4) by Ramiro Gómez).
- Add support for using Jinja2 template tags in content body Added filesource template function to render content of a given file ([0b66f14](https://github.com/yaph/logya/commit/0b66f14961c0fd5dda09432420e7f29b48a6e48d) by Ramiro Gómez).
- added comment for clarity ([bf43912](https://github.com/yaph/logya/commit/bf43912af345ea147f65e194559bab345227bbe4) by Ramiro Gómez).
- added missing packages and updated packages ([6866b63](https://github.com/yaph/logya/commit/6866b6377fce7b175a0df10edb85809541bb54e8) by Ramiro Gómez).
- added col-2 class, use it on sitemap ([e45db3c](https://github.com/yaph/logya/commit/e45db3c32ac89d77d407ace5334f26a426bb19a9) by Ramiro Gómez).
- added custom 404 page, set og:image if image and removed base_url from base template ([f8b2920](https://github.com/yaph/logya/commit/f8b29203888d422af20df5ab2d5a776af8a2587b) by Ramiro Gómez).
- added link to main rss feed, use logya logo as default favicon ([f9183a8](https://github.com/yaph/logya/commit/f9183a82b5e1c91dff903e9ba6ac000ddbcbd11b) by Ramiro Gómez).
- added .htaccess files, jquery script tags and scripts and styles template blocks ([c8c39d9](https://github.com/yaph/logya/commit/c8c39d95152efeafb46a4cea9d6d8c012f0adcdd) by Ramiro Gómez).
- added new starter site and removed docs site ([c4dcd8d](https://github.com/yaph/logya/commit/c4dcd8d116b5fd9b5338cdbc6c49a6b8ad49954a) by Ramiro Gómez).
- added hint that XML file contents are not parsed ([78620a7](https://github.com/yaph/logya/commit/78620a7b2a04955382871ace4f809e4b824b6277) by Ramiro Gomez).
- added release script ([e19fbe1](https://github.com/yaph/logya/commit/e19fbe1a50fc31a74ad9fa3859e7c484d367f710) by Ramiro Gomez).
- added idea ([1cabf8a](https://github.com/yaph/logya/commit/1cabf8afcb0907723bb4e9850b80bf14d81c1eaf) by Ramiro Gomez).
- added support for content written in markdown #gklst ([7d26940](https://github.com/yaph/logya/commit/7d26940640de79bb83b389d1bff0b5ab6dcc80a0) by Ramiro Gomez).
- added canonical template var, base_url setting in site.cfg is now required, added jinja2 urlencode filter #gklst ([9fdc750](https://github.com/yaph/logya/commit/9fdc75014fe033db32dbfad5bbe42784fcace502) by Ramiro Gomez).
- added __index__index for RSS generation and possible other stuff like sitemaps etc. ([67b8043](https://github.com/yaph/logya/commit/67b8043ae6d1f5a0d76b4bd0c8f6db021690ddf9) by Ramiro Gomez).
- added todos for v2.0 ([0c51b71](https://github.com/yaph/logya/commit/0c51b71374cb08aae5afd20508b667a5d6f5296f) by Ramiro Gomez).
- added tags documentation ([65b2ffc](https://github.com/yaph/logya/commit/65b2ffcab024375cf3a10d04cea225aaf6689bc0) by Ramiro Gomez).
- added issue ([e1044dc](https://github.com/yaph/logya/commit/e1044dce8ba304745902f24123c7a35b07bfc469) by Ramiro Gomez).
- added doc ([e6e2835](https://github.com/yaph/logya/commit/e6e28359d2d2e49b195860a6827d0c97e0f199b6) by Ramiro Gomez).
- added missing end of license ([1eb9db5](https://github.com/yaph/logya/commit/1eb9db5a043cca30706922c209534eaab0db3645) by Ramiro Gomez).
- added unittest to scm ([d7fbd99](https://github.com/yaph/logya/commit/d7fbd993d9e00f470e43a626985deaeaafbdf1d9) by Ramiro Gomez).
- added unittest for FileWriter.get_canonical_filename() ([c69fedf](https://github.com/yaph/logya/commit/c69fedfc62efb483cacff7ae6f16bc7fe827cc0e) by Ramiro Gomez).
- added new methods to make it easier to refresh auto-generated indexes ([fa2b48b](https://github.com/yaph/logya/commit/fa2b48b4a0d37b2ea29f4ff1a7290851c381d41b) by Ramiro Gomez).
- added TODO and documentation ([6563627](https://github.com/yaph/logya/commit/6563627582f68d7efc44111df4c33519f04f3aaf) by Ramiro Gomez).
- added docstrings ([b5c906e](https://github.com/yaph/logya/commit/b5c906e62a7ff57d8d948a734514ed22cb7917e9) by Ramiro Gomez).
- added exclude option to exclude headings , e.g. h1, to jquery.headerindex.js ([9f72a67](https://github.com/yaph/logya/commit/9f72a67778d5906ff342943004d2daff82636c51) by Ramiro Gomez).
- added base_path ([f702fb1](https://github.com/yaph/logya/commit/f702fb198cb4efcbefe68231758cb568983dbefa) by Ramiro Gomez).
- added TODO ([a04c128](https://github.com/yaph/logya/commit/a04c128c5fb70d3ba4ae90735cc27868ec751f39) by Ramiro Gomez).
- added --host and --port options to serve sub command ([78afd2a](https://github.com/yaph/logya/commit/78afd2ab830be7c15c0987f532e731e2f0e5c374) by Ramiro Gomez).
- added sublime project files to gitignore ([d4aa406](https://github.com/yaph/logya/commit/d4aa40623604f54a749475d3f278d9eeee7477e0) by Ramiro Gomez).
- added disqus template, get and set functions for module name in Extension class, set function for current directory in Geeklog, unit test class for extension directory ([86fa00a](https://github.com/yaph/logya/commit/86fa00aca327a2ef47edc3d20b8b53fffbe236ee) by Ramiro Gomez).
- added gen and help aliases ([1bd582e](https://github.com/yaph/logya/commit/1bd582e071647f9d59d1661157dd5dcb273d6493) by Ramiro Gomez).
- added custom stylesheet with Bootstrap overrides; copy static dir to target site ([2be4005](https://github.com/yaph/logya/commit/2be4005d81e1915e919494edcb26bb5e6d21ff20) by Ramiro Gomez).
- added files for distribution and use jinja2 ([319b6d3](https://github.com/yaph/logya/commit/319b6d301ba7832be9c29c7e8b531d946f808dc2) by Ramiro Gomez).

### Fixed

- fixed rst link added new logo concept ([4a68afb](https://github.com/yaph/logya/commit/4a68afbf337c09ea072017d48bf63b151ce059c2) by Ramiro Gómez).
- Fixed #49: removed server.log file, log to default stream instead. ([6b93d84](https://github.com/yaph/logya/commit/6b93d84ef45f3831a811eee1f661c0c68197b181) by Ramiro Gómez).
- Fixed #50: added option to trim whitespace in templates. ([492238a](https://github.com/yaph/logya/commit/492238ad50b964a879d982782c80d3cd7bf21dda) by Ramiro Gómez).
- Fixed #77: set canonical for index pages ([a88adac](https://github.com/yaph/logya/commit/a88adac4d6045077d0dfa69474f489feaa82308d) by Ramiro Gómez).
- Fixed #62: moved test content to tests ([b4db23c](https://github.com/yaph/logya/commit/b4db23c0cd0ceb801f6e89d45a3d289af5af055b) by Ramiro Gómez).
- Fixed typo. ([d7402f6](https://github.com/yaph/logya/commit/d7402f6e01570ea3c83bf821f9f7b9f088e53626) by Ramiro Gómez).
- Fixed markup. ([fe76062](https://github.com/yaph/logya/commit/fe76062b03e1fde3cee60ff8d858383c89784864) by Ramiro Gómez).
- Fixed #76: renamed docs_parsed to docs. ([2713d85](https://github.com/yaph/logya/commit/2713d8574bcdd314e4ce8aecebe8df9da7909274) by Ramiro Gómez).
- Fixed #72: template settings for collections is now effective. ([64d097a](https://github.com/yaph/logya/commit/64d097a3e9362db2ba381cfdefa99f133ac296b0) by Ramiro Gómez).
- Fixed #67: document allowed extensions- ([cf2aaa7](https://github.com/yaph/logya/commit/cf2aaa718a6160f05b3228dcd331dd082a082840) by Ramiro Gómez).
- Fixed #65 add dir_site argument to set logya.dir_site, which has replaced dir_current. ([aab0ca4](https://github.com/yaph/logya/commit/aab0ca4258a50205ca0b9002455c270a28dad74b) by Ramiro Gómez).
- Fixed import and call to target_filto target_file ([4c24fea](https://github.com/yaph/logya/commit/4c24fea5f8c42cc37791ff2ad4e3f8d1a5271776) by Ramiro Gómez).
- Fix #57 remove deploy script to avoid future desasters. ([fea4eb0](https://github.com/yaph/logya/commit/fea4eb03115f7ee18fc4164564ce0adffde65bbf) by Ramiro Gómez).
- Fixed #58: removed url setting from sample about page. ([7ea5964](https://github.com/yaph/logya/commit/7ea59648b0d79577a8ec2c0a26ac5dde705c1c49) by Ramiro Gómez).
- Fixed #47: Removed urlencode template filter as it is included in the required jinja2 version. ([223d054](https://github.com/yaph/logya/commit/223d054906209a862f99bd4af0747ec1a6e6d8e7) by Ramiro Gómez).
- Fix #54: use % formatting in logging functions ([046c60e](https://github.com/yaph/logya/commit/046c60ebdcb125077762dc6b02a1851ad885a202) by Ramiro Gómez).
- Fix #55: dont use list comprehension where not needed. ([2ca1973](https://github.com/yaph/logya/commit/2ca19738cf628e29ae84263f75efac9c1e172049) by Ramiro Gómez).
- Fix #53: Finished moving path logic form core to path. ([9b4df86](https://github.com/yaph/logya/commit/9b4df861809b88e7af40bf3c34bcbd8048d7abe9) by Ramiro Gómez).
- Fixed #48: Use .htaccess from HTML5 Boilerplate. ([7cb8c6a](https://github.com/yaph/logya/commit/7cb8c6abe1305863c8024bfd9fa383c0fae36a0f) by Ramiro Gómez).
- fixed wrong variable name that caused markdown not to be parsed ([d94e43e](https://github.com/yaph/logya/commit/d94e43ea69a704205be13fe4ef7a2c72a2bb5565) by Ramiro Gómez).
- Fixed #39: added sample video macro dont display sharemenu links as buttons added fa icons for reddit and su ([17c9247](https://github.com/yaph/logya/commit/17c9247915689402a8b2988346752453a7b326fc) by Ramiro Gómez).
- fix #43: generate index of header properties as json as run example ([ab7d310](https://github.com/yaph/logya/commit/ab7d3106b9b1322ad0a1fe623337a33402d6c2de) by Ramiro Gómez).
- fix #42 added run command ([3d765e6](https://github.com/yaph/logya/commit/3d765e6226d32dfec02040b9469456306a400572) by Ramiro Gómez).
- fix #38 document get_doc tempate function ([3a18197](https://github.com/yaph/logya/commit/3a181974ae5049df95c721b89a5502a087e0d5dd) by Ramiro Gómez).
- fix #35: added documentation for urlencode and filesource ([758a705](https://github.com/yaph/logya/commit/758a7056db0fbf89c172ead7fd2df0c76b04f73f) by Ramiro Gómez).
- fix #34: set debug variable to True in serve mode ([75f57ae](https://github.com/yaph/logya/commit/75f57ae3f87602aa5470bbe4475213e589866eac) by Ramiro Gómez).
- fix #31: replace slashes in index path values ([0d3d463](https://github.com/yaph/logya/commit/0d3d463e4637a1da491f62529005697fcfd7a9aa) by Ramiro Gómez).
- fix #27 generate indexes from site config, renamed items to get_section in config which now returns section dict ([2c8a6fb](https://github.com/yaph/logya/commit/2c8a6fbaed41ecd861620caeb8ff995db6f611b0) by Ramiro Gómez).
- fixed to config bugs and added site.yaml ([7f3d2f1](https://github.com/yaph/logya/commit/7f3d2f1cf2191693600f5550e7c3ea747e73f731) by Ramiro Gómez).
- fixed exploring data link ([d56e70a](https://github.com/yaph/logya/commit/d56e70a87587239e97787452fc934b14cac322fa) by Ramiro Gómez).
- fixed channel link url in RSS feed ([1e8bcf4](https://github.com/yaph/logya/commit/1e8bcf4c1acc437b0c39957e6c194a9cee8d127d) by Ramiro Gómez).
- fix #21: only consider files with allowed ext when reading files ([5faff98](https://github.com/yaph/logya/commit/5faff98419110e35305e1aaa4a8096b32206fc0e) by Ramiro Gómez).
- fix script reference ([6bbb794](https://github.com/yaph/logya/commit/6bbb79443c8f8f4c09ed83d34ec0dbba219ecc9c) by Ramiro Gómez).
- fix #12 set local server and port as base_url in serve mode ([ebb6912](https://github.com/yaph/logya/commit/ebb69120d3778598c946927606a19d10e4f1a01d) by Ramiro Gómez).
- fix #4 using new rss template and jinja2 not more dependent on PyRSS2Gen added url back as optional param to _update_indexes ([a8bda10](https://github.com/yaph/logya/commit/a8bda10bf1e3696036918e8da1c12634577fb3e6) by Ramiro Gómez).
- fix #11 main object now in core.py ([c31018f](https://github.com/yaph/logya/commit/c31018f1776e7efcbb865092c5e3ade20db8debc) by Ramiro Gómez).
- fix #13 warn users when url was used before ([c9011f1](https://github.com/yaph/logya/commit/c9011f1950f5cb74e437d4f3d2d835a7c2efb617) by Ramiro Gómez).
- fixed encoding troubles for python 2.7 ([c9b40fa](https://github.com/yaph/logya/commit/c9b40fa073d2334d5c6ee9539f0a9583d3932d2f) by Ramiro Gómez).
- fix bug #7 by specifying number directly in setup.py, find a better way ([768f235](https://github.com/yaph/logya/commit/768f23545d8233af7d9d56516a8c969780e0600f) by Ramiro Gómez).
- fix issue #3: use only path component of static files and ignore possible query params ([3c0de1b](https://github.com/yaph/logya/commit/3c0de1beebcf8646747a106d7c3528e2f233361f) by Ramiro Gomez).
- fixed references to README ([959af96](https://github.com/yaph/logya/commit/959af965865467a57f550c6d5cbfec1966e02592) by Ramiro Gomez).
- fixed dupliace install_requires and updated to 2.0alpha ([3c0e79e](https://github.com/yaph/logya/commit/3c0e79ebaf09195fe0769ba1d106a4a19478546b) by Ramiro Gomez).
- fixed css issue with fixed header and doc links ([6be8374](https://github.com/yaph/logya/commit/6be8374e7185772d7256e9b3b4867a5556e91cf3) by Ramiro Gomez).
- fixed existing tests and run all tests ([4835184](https://github.com/yaph/logya/commit/4835184e46d6322343359caa2c7423d0d99c3a5f) by Ramiro Gomez).
- fixed bug and made code simpler ([68cdad4](https://github.com/yaph/logya/commit/68cdad4eaffbff0899950427744165ed0ecf6b45) by Ramiro Gomez).
- fixed gen sup parser bug ([55f8d41](https://github.com/yaph/logya/commit/55f8d419afbf5d7f7a114e68c1c54e618c455bdb) by Ramiro Gomez).

### Changed

- Changed version ([f17b066](https://github.com/yaph/logya/commit/f17b066f1e12d254985aeb4354a57a6476049db5) by Ramiro Gómez).
- Changed logya homepage ([454b57c](https://github.com/yaph/logya/commit/454b57ccaa92241e390fc6e80b56d11968034350) by Ramiro Gómez).
- changelog ([cba2dcd](https://github.com/yaph/logya/commit/cba2dcd4f0a0b5f73ffab34d862b445ddc05c8c4) by Ramiro Gómez).
- changed travis notifications ([7188115](https://github.com/yaph/logya/commit/718811582ac161ebe79c3b5998ec48e57dd85736) by Ramiro Gómez).
- changed base path for docs site ([56c9ded](https://github.com/yaph/logya/commit/56c9ded374ce883e68ecd5bd14efc40b242b7059) by Ramiro Gomez).
- changed import ([8b4170f](https://github.com/yaph/logya/commit/8b4170ffab36f24cf5dfcf955e00b468c6a409ac) by Ramiro Gomez).
- changed setup url and removed download_url ([1ae9af2](https://github.com/yaph/logya/commit/1ae9af2f4349ab7f743cc1ebb883d527d3dbddda) by Ramiro Gomez).
- changed README added jinja2 as requirement ([4178ad7](https://github.com/yaph/logya/commit/4178ad7d7a30f6ba4877812ead2bec75e66865ca) by Ramiro Gomez).
- changed command ([ad8555a](https://github.com/yaph/logya/commit/ad8555af8686978623d27018468ed50dd993b598) by Ramiro Gomez).

### Removed

- removed distribute_setup.py from MANIFEST ([cdb019a](https://github.com/yaph/logya/commit/cdb019afbb3369321f4169068c74496e4da03213) by Ramiro Gómez).
- removed read function in docreader added markdown_attr_list test ([d82fc54](https://github.com/yaph/logya/commit/d82fc5499b1c4353b456be8ce045e7ecec7575f7) by Ramiro Gómez).
- remove t on clean ([8ccc6b7](https://github.com/yaph/logya/commit/8ccc6b7ba13ace4d11461b1e345982f6e0b20d10) by Ramiro Gómez).
- remove unused keyword argument "modified" ([bd50e0b](https://github.com/yaph/logya/commit/bd50e0ba4efd139094de69fb08e9a93848004915) by Ramiro Gómez).
- removed unnecessary requirements ([a43cbc6](https://github.com/yaph/logya/commit/a43cbc6920727cf9b9527817f9c7ee91cc18efe6) by Ramiro Gómez).
- Removed all_vars and doc_vars from Template. Document body variable. ([832f5ce](https://github.com/yaph/logya/commit/832f5cedfb464a0288212cc57a4e422476df0b92) by Ramiro Gómez).
- Removed Config class, the config module now consits of load and search_dict_list functions. ([f502402](https://github.com/yaph/logya/commit/f5024020897de4939c22605eb9ba3226d6e56ad0) by Ramiro Gómez).
- Removed unused import. ([8407c0b](https://github.com/yaph/logya/commit/8407c0b8621f7550473433a4573e578d8ecc5042) by Ramiro Gómez).
- Removed call to read in with clause ([fb64fcc](https://github.com/yaph/logya/commit/fb64fccf8f02deea6cd2ae284eacccc2ce1f245f) by Ramiro Gómez).
- Removed FileWriter class entirely. ([b5ee0ab](https://github.com/yaph/logya/commit/b5ee0aba05b048486ac462c58e7c4702e33f0469) by Ramiro Gómez).
- removed unused rules and comments from default htaccess ([5c96999](https://github.com/yaph/logya/commit/5c969995813983bcf7b15a111671119d4c3d6462) by Ramiro Gómez).
- removed whitespace ([3ca45d2](https://github.com/yaph/logya/commit/3ca45d2f73a1672d68085e28dec4bbc284058da2) by Ramiro Gómez).
- removed unused function ([f26bfa3](https://github.com/yaph/logya/commit/f26bfa34a96cef929a9e3ab089a807590755d6bb) by Ramiro Gómez).
- removed duplicate info from doc ([f69b5ec](https://github.com/yaph/logya/commit/f69b5ec720caaed539e6df07197ba0865b642fe7) by Ramiro Gómez).
- removed clearfix class which is available in bootstrap ([9db59f6](https://github.com/yaph/logya/commit/9db59f6e09b05793c937a502b51c7540f7cbb0fc) by Ramiro Gómez).
- removed ref to old file name from travis install command removed deprecated --use-mirrors option from travis install command ([16774b5](https://github.com/yaph/logya/commit/16774b524478699f753bbb80e2ee98a72462d125) by Ramiro Gómez).
- removed JSONencoder from writer ([13d59bb](https://github.com/yaph/logya/commit/13d59bbfa842f055b025d923a425482a8a86b88f) by Ramiro Gómez).
- removed json variable again, doesnt really make sense if not all variables can be provided due to slowing down everything like hell ([62444dd](https://github.com/yaph/logya/commit/62444dda3e0f28065d583e832a69c9de2af5a535) by Ramiro Gómez).
- removed disqus from tests too ([6c44d52](https://github.com/yaph/logya/commit/6c44d5204a880936e4b0003cbebffb3d6589b480) by Ramiro Gómez).
- removed unused imports ([6bafd25](https://github.com/yaph/logya/commit/6bafd2543ec6cb0c07cd26ec6f80f55c5868268d) by Ramiro Gómez).
- removed useless section ([a21da70](https://github.com/yaph/logya/commit/a21da70e6214aeb5dc5c3ea0484d72e7404d3c33) by Ramiro Gómez).
- removed broken github download link and amended docs ([16b6fda](https://github.com/yaph/logya/commit/16b6fdaad8e0d9248c81379cb64264ff2c117400) by Ramiro Gómez).
- removed sub heading ([637e6d2](https://github.com/yaph/logya/commit/637e6d2b0e5b5ca6176ff71ddf7420b6080876ea) by Ramiro Gomez).
- removed unused imports and added missing docstrings ([27f863f](https://github.com/yaph/logya/commit/27f863f5747a20209050bedda7f0e083b4878244) by Ramiro Gomez).
- remove existing deploy dir in generate mode then copy static files, copy content of source static directly to deploy root ([bd1c0ce](https://github.com/yaph/logya/commit/bd1c0ced1b1c353b1018b360cef806b67ccda6dd) by Ramiro Gomez).
- removed empty lines ([28b89a4](https://github.com/yaph/logya/commit/28b89a4e4bee015e4a655cac533e2ad0ae69ce86) by Ramiro Gomez).
- removed help sub command, more concise arg processing ([dc2ff3b](https://github.com/yaph/logya/commit/dc2ff3b287b916f9ec74d657093b1e190dce7c8d) by Ramiro Gomez).
- removed sample_page1 changed templates set base_path via configuration ([911fbbb](https://github.com/yaph/logya/commit/911fbbba8d43992f7062c337f6df7ed19b5ee9c8) by Ramiro Gomez).
- removed copy of doc.html ([315a004](https://github.com/yaph/logya/commit/315a004cf99f23e7e897273491fb584e9603512d) by Ramiro Gomez).

