(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./$$_lazy_route_resource lazy recursive":
/*!******************************************************!*\
  !*** ./$$_lazy_route_resource lazy namespace object ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./src/app/app-footer/app-footer.component.ts":
/*!****************************************************!*\
  !*** ./src/app/app-footer/app-footer.component.ts ***!
  \****************************************************/
/*! exports provided: AppFooterComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppFooterComponent", function() { return AppFooterComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");



const _c0 = function () { return ["/deklaracja-dostepnosci"]; };
const _c1 = function () { return [""]; };
class AppFooterComponent {
    constructor() { }
    ngOnInit() {
    }
    openInstructions() {
        window.open("/assets/MSiG_2_0_-_Instrukcja_użytkownika_systemu_v1.0.pdf");
    }
}
AppFooterComponent.ɵfac = function AppFooterComponent_Factory(t) { return new (t || AppFooterComponent)(); };
AppFooterComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: AppFooterComponent, selectors: [["app-footer"]], decls: 13, vars: 4, consts: [[1, "version"], [1, "instructions"], ["aria-label", "Instrukcja u\u017Cytkowania", "alt", "Instrukcja u\u017Cytkowania", "href", "", 3, "keyup.enter", "click"], [1, "declaration"], ["aria-label", "przejd\u017A deklaracji dost\u0119pno\u015Bci", "alt", "Deklaracja dost\u0119pno\u015Bci", "role", "link", 3, "routerLink"], [1, "logo-footer"], ["aria-label", "przejd\u017A do g\u0142\u00F3wnego widoku", "alt", "logo Ministerstwa Sprawiedliwo\u015Bci", 1, "gov-pl", 3, "routerLink"]], template: function AppFooterComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "footer");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, " \u00A9 2022 Wszystkie prawa zastrze\u017Cone ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4, " Wersja: 1.0.1 ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "a", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function AppFooterComponent_Template_a_keyup_enter_6_listener() { return ctx.openInstructions(); })("click", function AppFooterComponent_Template_a_click_6_listener() { return ctx.openInstructions(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "Instrukcja u\u017Cytkowania");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "div", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "a", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](10, "Deklaracja dost\u0119pno\u015Bci");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "div", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "a", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction0"](2, _c0));
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction0"](3, _c1));
    } }, directives: [_angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterLinkWithHref"]], styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2FwcC1mb290ZXIvYXBwLWZvb3Rlci5jb21wb25lbnQuc2NzcyJ9 */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AppFooterComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-footer',
                templateUrl: './app-footer.component.html',
                styleUrls: ['./app-footer.component.scss']
            }]
    }], function () { return []; }, null); })();


/***/ }),

/***/ "./src/app/app-routing.module.ts":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var _declaration_declaration_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./declaration/declaration.component */ "./src/app/declaration/declaration.component.ts");
/* harmony import */ var _list_by_year_list_by_year_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./list-by-year/list-by-year.component */ "./src/app/list-by-year/list-by-year.component.ts");
/* harmony import */ var _search_form_search_form_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./search-form/search-form.component */ "./src/app/search-form/search-form.component.ts");
/* harmony import */ var _table_list_table_list_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./table-list/table-list.component */ "./src/app/table-list/table-list.component.ts");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");








const routes = [
    {
        path: '',
        component: _search_form_search_form_component__WEBPACK_IMPORTED_MODULE_2__["SearchFormComponent"],
        pathMatch: 'full'
    },
    {
        path: 'list',
        component: _table_list_table_list_component__WEBPACK_IMPORTED_MODULE_3__["TableListComponent"],
        pathMatch: 'full'
    },
    {
        path: 'pobieranie-monitora/:year',
        component: _list_by_year_list_by_year_component__WEBPACK_IMPORTED_MODULE_1__["ListByYearComponent"],
        pathMatch: 'full'
    },
    {
        path: 'deklaracja-dostepnosci',
        component: _declaration_declaration_component__WEBPACK_IMPORTED_MODULE_0__["DeclarationComponent"],
        pathMatch: 'full'
    },
    {
        path: 'assets/MSiG_2_0_-_Instrukcja_użytkownika_systemu_v1.0.pdf',
        redirectTo: 'assets/MSiG_2_0_-_Instrukcja_użytkownika_systemu_v1.0.pdf'
    },
    {
        path: '**',
        redirectTo: '',
        component: _search_form_search_form_component__WEBPACK_IMPORTED_MODULE_2__["SearchFormComponent"]
    }
];
class AppRoutingModule {
}
AppRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_4__["ɵɵdefineNgModule"]({ type: AppRoutingModule });
AppRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_4__["ɵɵdefineInjector"]({ factory: function AppRoutingModule_Factory(t) { return new (t || AppRoutingModule)(); }, imports: [[_angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterModule"].forRoot(routes)], _angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterModule"]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_4__["ɵɵsetNgModuleScope"](AppRoutingModule, { imports: [_angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterModule"]], exports: [_angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterModule"]] }); })();
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_4__["ɵsetClassMetadata"](AppRoutingModule, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_4__["NgModule"],
        args: [{
                imports: [_angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterModule"].forRoot(routes)],
                exports: [_angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterModule"]]
            }]
    }], null, null); })();


/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _shared_alert_alert_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./shared/alert/alert.component */ "./src/app/shared/alert/alert.component.ts");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _services_state_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./services/state.service */ "./src/app/services/state.service.ts");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/http.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
/* harmony import */ var _app_footer_app_footer_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./app-footer/app-footer.component */ "./src/app/app-footer/app-footer.component.ts");








const _c0 = ["alertContainer"];
function AppComponent_ng_template_0_Template(rf, ctx) { }
class AppComponent {
    constructor(componentFactoryResolver, state, document, http) {
        this.componentFactoryResolver = componentFactoryResolver;
        this.state = state;
        this.document = document;
        this.http = http;
        this.title = 'msig';
    }
    ngOnInit() {
        this.getApiUrl();
        this.state.alertBody$.subscribe((body) => {
            this.alertBody = body;
            this.alertMessage();
        });
    }
    getApiUrl() {
        let url = `${document.location.origin}/`;
        this.http.get(`${url}home/getapiurl`, { responseType: 'text' }).subscribe({
            next: res => {
                this.state.shareUrl(res);
                this.setUrlToStorage(res);
            },
            error: err => {
                console.log(err);
            }
        });
    }
    setUrlToStorage(url) {
        sessionStorage.setItem('API_URL', url);
    }
    alertMessage() {
        if (this.alertrContainer.get(0) !== null) {
            return;
        }
        const alerComponent = this.componentFactoryResolver.
            resolveComponentFactory(_shared_alert_alert_component__WEBPACK_IMPORTED_MODULE_0__["AlertComponent"]);
        const alertInfoRef = this.alertrContainer.createComponent(alerComponent);
        alertInfoRef.instance.alertConf = this.alertBody;
        alertInfoRef.instance.closedAlert.subscribe(close => {
            this.alertrContainer.clear();
        });
        this.alertInstance = alertInfoRef;
    }
}
AppComponent.ɵfac = function AppComponent_Factory(t) { return new (t || AppComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_1__["ComponentFactoryResolver"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_services_state_service__WEBPACK_IMPORTED_MODULE_3__["StateService"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_common__WEBPACK_IMPORTED_MODULE_2__["DOCUMENT"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_4__["HttpClient"])); };
AppComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineComponent"]({ type: AppComponent, selectors: [["app-root"]], viewQuery: function AppComponent_Query(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵstaticViewQuery"](_c0, true, _angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewContainerRef"]);
    } if (rf & 2) {
        var _t;
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵloadQuery"]()) && (ctx.alertrContainer = _t.first);
    } }, decls: 6, vars: 0, consts: [["alertContainer", ""], [1, "layout"], [1, "msig-wraper"]], template: function AppComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](0, AppComponent_ng_template_0_Template, 0, 0, "ng-template", null, 0, _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplateRefExtractor"]);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](2, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "div", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](4, "router-outlet");
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](5, "app-footer");
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    } }, directives: [_angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterOutlet"], _app_footer_app_footer_component__WEBPACK_IMPORTED_MODULE_6__["AppFooterComponent"]], styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2FwcC5jb21wb25lbnQuc2NzcyJ9 */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](AppComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"],
        args: [{
                selector: 'app-root',
                templateUrl: './app.component.html',
                styleUrls: ['./app.component.scss']
            }]
    }], function () { return [{ type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ComponentFactoryResolver"] }, { type: _services_state_service__WEBPACK_IMPORTED_MODULE_3__["StateService"] }, { type: undefined, decorators: [{
                type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Inject"],
                args: [_angular_common__WEBPACK_IMPORTED_MODULE_2__["DOCUMENT"]]
            }] }, { type: _angular_common_http__WEBPACK_IMPORTED_MODULE_4__["HttpClient"] }]; }, { alertrContainer: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewChild"],
            args: ['alertContainer', { read: _angular_core__WEBPACK_IMPORTED_MODULE_1__["ViewContainerRef"], static: true }]
        }] }); })();


/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: options, AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "options", function() { return options; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _shared_alert_alert_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./shared/alert/alert.component */ "./src/app/shared/alert/alert.component.ts");
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/__ivy_ngcc__/fesm2015/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./app-routing.module */ "./src/app/app-routing.module.ts");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
/* harmony import */ var _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @ng-bootstrap/ng-bootstrap */ "./node_modules/@ng-bootstrap/ng-bootstrap/__ivy_ngcc__/fesm2015/ng-bootstrap.js");
/* harmony import */ var _date_picker_date_picker_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./date-picker/date-picker.component */ "./src/app/date-picker/date-picker.component.ts");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
/* harmony import */ var _table_list_table_list_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./table-list/table-list.component */ "./src/app/table-list/table-list.component.ts");
/* harmony import */ var _search_form_search_form_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./search-form/search-form.component */ "./src/app/search-form/search-form.component.ts");
/* harmony import */ var _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./main-header/main-header.component */ "./src/app/main-header/main-header.component.ts");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/http.js");
/* harmony import */ var ngx_mask__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ngx-mask */ "./node_modules/ngx-mask/__ivy_ngcc__/fesm2015/ngx-mask.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _angular_common_locales_pl__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @angular/common/locales/pl */ "./node_modules/@angular/common/locales/pl.js");
/* harmony import */ var _angular_common_locales_pl__WEBPACK_IMPORTED_MODULE_14___default = /*#__PURE__*/__webpack_require__.n(_angular_common_locales_pl__WEBPACK_IMPORTED_MODULE_14__);
/* harmony import */ var _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! ./shared/fullsize-loader/fullsize-loader.component */ "./src/app/shared/fullsize-loader/fullsize-loader.component.ts");
/* harmony import */ var _list_by_year_list_by_year_component__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! ./list-by-year/list-by-year.component */ "./src/app/list-by-year/list-by-year.component.ts");
/* harmony import */ var _services_Interceptor__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ./services/Interceptor */ "./src/app/services/Interceptor.ts");
/* harmony import */ var _services_format_bytes_pipe__WEBPACK_IMPORTED_MODULE_18__ = __webpack_require__(/*! ./services/format-bytes.pipe */ "./src/app/services/format-bytes.pipe.ts");
/* harmony import */ var _app_footer_app_footer_component__WEBPACK_IMPORTED_MODULE_19__ = __webpack_require__(/*! ./app-footer/app-footer.component */ "./src/app/app-footer/app-footer.component.ts");
/* harmony import */ var _declaration_declaration_component__WEBPACK_IMPORTED_MODULE_20__ = __webpack_require__(/*! ./declaration/declaration.component */ "./src/app/declaration/declaration.component.ts");























const options = null;
Object(_angular_common__WEBPACK_IMPORTED_MODULE_13__["registerLocaleData"])(_angular_common_locales_pl__WEBPACK_IMPORTED_MODULE_14___default.a, 'pl');
class AppModule {
}
AppModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: AppModule, bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_4__["AppComponent"]] });
AppModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ factory: function AppModule_Factory(t) { return new (t || AppModule)(); }, providers: [
        {
            provide: _angular_core__WEBPACK_IMPORTED_MODULE_2__["LOCALE_ID"],
            useValue: "pl-PL"
        },
        {
            provide: _angular_common_http__WEBPACK_IMPORTED_MODULE_11__["HTTP_INTERCEPTORS"],
            useClass: _services_Interceptor__WEBPACK_IMPORTED_MODULE_17__["MyInterceptor"],
            multi: true
        }
    ], imports: [[
            _angular_common__WEBPACK_IMPORTED_MODULE_13__["CommonModule"],
            _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__["BrowserModule"],
            _app_routing_module__WEBPACK_IMPORTED_MODULE_3__["AppRoutingModule"],
            _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_5__["NgbModule"],
            _angular_forms__WEBPACK_IMPORTED_MODULE_7__["FormsModule"],
            _angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"],
            _angular_common_http__WEBPACK_IMPORTED_MODULE_11__["HttpClientModule"],
            ngx_mask__WEBPACK_IMPORTED_MODULE_12__["NgxMaskModule"].forRoot(),
        ], _angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"],
        _angular_forms__WEBPACK_IMPORTED_MODULE_7__["FormsModule"]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](AppModule, { declarations: [_shared_alert_alert_component__WEBPACK_IMPORTED_MODULE_0__["AlertComponent"],
        _app_component__WEBPACK_IMPORTED_MODULE_4__["AppComponent"],
        _date_picker_date_picker_component__WEBPACK_IMPORTED_MODULE_6__["DatePickerComponent"],
        _table_list_table_list_component__WEBPACK_IMPORTED_MODULE_8__["TableListComponent"],
        _search_form_search_form_component__WEBPACK_IMPORTED_MODULE_9__["SearchFormComponent"],
        _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_10__["MainHeaderComponent"],
        _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_15__["FullsizeLoaderComponent"],
        _list_by_year_list_by_year_component__WEBPACK_IMPORTED_MODULE_16__["ListByYearComponent"],
        _services_format_bytes_pipe__WEBPACK_IMPORTED_MODULE_18__["FormatBytesPipe"],
        _app_footer_app_footer_component__WEBPACK_IMPORTED_MODULE_19__["AppFooterComponent"],
        _declaration_declaration_component__WEBPACK_IMPORTED_MODULE_20__["DeclarationComponent"]], imports: [_angular_common__WEBPACK_IMPORTED_MODULE_13__["CommonModule"],
        _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__["BrowserModule"],
        _app_routing_module__WEBPACK_IMPORTED_MODULE_3__["AppRoutingModule"],
        _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_5__["NgbModule"],
        _angular_forms__WEBPACK_IMPORTED_MODULE_7__["FormsModule"],
        _angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"],
        _angular_common_http__WEBPACK_IMPORTED_MODULE_11__["HttpClientModule"], ngx_mask__WEBPACK_IMPORTED_MODULE_12__["NgxMaskModule"]], exports: [_angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"],
        _angular_forms__WEBPACK_IMPORTED_MODULE_7__["FormsModule"]] }); })();
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵsetClassMetadata"](AppModule, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_2__["NgModule"],
        args: [{
                declarations: [
                    _shared_alert_alert_component__WEBPACK_IMPORTED_MODULE_0__["AlertComponent"],
                    _app_component__WEBPACK_IMPORTED_MODULE_4__["AppComponent"],
                    _date_picker_date_picker_component__WEBPACK_IMPORTED_MODULE_6__["DatePickerComponent"],
                    _table_list_table_list_component__WEBPACK_IMPORTED_MODULE_8__["TableListComponent"],
                    _search_form_search_form_component__WEBPACK_IMPORTED_MODULE_9__["SearchFormComponent"],
                    _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_10__["MainHeaderComponent"],
                    _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_15__["FullsizeLoaderComponent"],
                    _list_by_year_list_by_year_component__WEBPACK_IMPORTED_MODULE_16__["ListByYearComponent"],
                    _services_format_bytes_pipe__WEBPACK_IMPORTED_MODULE_18__["FormatBytesPipe"],
                    _app_footer_app_footer_component__WEBPACK_IMPORTED_MODULE_19__["AppFooterComponent"],
                    _declaration_declaration_component__WEBPACK_IMPORTED_MODULE_20__["DeclarationComponent"],
                ],
                imports: [
                    _angular_common__WEBPACK_IMPORTED_MODULE_13__["CommonModule"],
                    _angular_platform_browser__WEBPACK_IMPORTED_MODULE_1__["BrowserModule"],
                    _app_routing_module__WEBPACK_IMPORTED_MODULE_3__["AppRoutingModule"],
                    _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_5__["NgbModule"],
                    _angular_forms__WEBPACK_IMPORTED_MODULE_7__["FormsModule"],
                    _angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"],
                    _angular_common_http__WEBPACK_IMPORTED_MODULE_11__["HttpClientModule"],
                    ngx_mask__WEBPACK_IMPORTED_MODULE_12__["NgxMaskModule"].forRoot(),
                ],
                entryComponents: [_shared_alert_alert_component__WEBPACK_IMPORTED_MODULE_0__["AlertComponent"]],
                exports: [
                    _angular_forms__WEBPACK_IMPORTED_MODULE_7__["ReactiveFormsModule"],
                    _angular_forms__WEBPACK_IMPORTED_MODULE_7__["FormsModule"]
                ],
                providers: [
                    {
                        provide: _angular_core__WEBPACK_IMPORTED_MODULE_2__["LOCALE_ID"],
                        useValue: "pl-PL"
                    },
                    {
                        provide: _angular_common_http__WEBPACK_IMPORTED_MODULE_11__["HTTP_INTERCEPTORS"],
                        useClass: _services_Interceptor__WEBPACK_IMPORTED_MODULE_17__["MyInterceptor"],
                        multi: true
                    }
                ],
                bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_4__["AppComponent"]]
            }]
    }], null, null); })();


/***/ }),

/***/ "./src/app/date-picker/date-picker.component.ts":
/*!******************************************************!*\
  !*** ./src/app/date-picker/date-picker.component.ts ***!
  \******************************************************/
/*! exports provided: DatePickerComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DatePickerComponent", function() { return DatePickerComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @ng-bootstrap/ng-bootstrap */ "./node_modules/@ng-bootstrap/ng-bootstrap/__ivy_ngcc__/fesm2015/ng-bootstrap.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");





class DatePickerComponent {
    constructor(config, calendar) {
        this.calendar = calendar;
        this.valueSelected = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
        config.outsideDays = 'hidden';
    }
    ngOnInit() {
    }
    selectToday() {
        this.modelDate = this.calendar.getToday();
    }
    ngOnChanges(changes) {
        if (changes.startValue) {
            this.setStartDate = null;
            this.setStartDate = changes.startValue.currentValue;
            if (this.setStartDate) {
                this.dateValue = null;
                setTimeout(() => {
                    //this.dateValue = `${this.setStartDate.year}-${this.setStartDate.month}-${this.setStartDate.day}`;
                    this.dateValue = this.formatForApi(`${this.setStartDate.year}-${this.setStartDate.month}-${this.setStartDate.day}`);
                }, 0);
            }
        }
        if (changes.minDate) {
            this.minDateRange = null;
            this.minDateRange = changes.minDate.currentValue;
        }
        if (changes.maxDate) {
            this.minDateRange = null;
            this.minDateRange = changes.maxDate.currentValue;
        }
    }
    formatForApi(date) {
        let d = new Date(date);
        let year = d.getFullYear();
        let month = ((d.getMonth() + 1) < 10 ? '0' : '') + (d.getMonth() + 1);
        let day = (d.getDate() < 10 ? '0' : '') + d.getDate();
        return `${year}-${month}-${day}`;
    }
    changePropertyValue() {
        let dateToChange = `${this.modelDate.year}-${this.modelDate.month}-${this.modelDate.day}`;
        let d = new Date(`${this.modelDate.year}-${this.modelDate.month}-${this.modelDate.day}`);
        this.valueSelected.emit(this.formatForApi(dateToChange));
    }
}
DatePickerComponent.ɵfac = function DatePickerComponent_Factory(t) { return new (t || DatePickerComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbInputDatepickerConfig"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbCalendar"])); };
DatePickerComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: DatePickerComponent, selectors: [["app-date-picker"]], inputs: { popoverText: ["popover", "popoverText"], startValue: "startValue", minDateRange: ["minDate", "minDateRange"], maxDateRange: ["maxDate", "maxDateRange"], valueSelected: ["rangeTo", "valueSelected"] }, outputs: { valueSelected: "valueSelected" }, features: [_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵProvidersFeature"]([_ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbInputDatepickerConfig"]]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵNgOnChangesFeature"]], decls: 9, vars: 5, consts: [[1, "form-group"], [1, "input-group"], ["name", "dp", "ngbDatepicker", "", "aria-label", "Wybierz dat\u0119 z kalendarza", "alt", "Wybierz dat\u0119", "readonly", "", 1, "form-control", 3, "minDate", "startDate", "maxDate", "ngModel", "value", "ngModelChange", "dateSelect"], ["d", "ngbDatepicker"], [1, "input-group-append"], ["type", "button", 1, "btn", "btn-outline-secondary", "calendar", 2, "padding-left", "16px", 3, "click"], ["xmlns", "http://www.w3.org/2000/svg", "width", "18", "height", "18", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-calendar3"], ["d", "M14 0H2a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2zM1 3.857C1 3.384 1.448 3 2 3h12c.552 0 1 .384 1 .857v10.286c0 .473-.448.857-1 .857H2c-.552 0-1-.384-1-.857V3.857z"], ["d", "M6.5 7a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm-9 3a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2zm3 0a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"]], template: function DatePickerComponent_Template(rf, ctx) { if (rf & 1) {
        const _r1 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "input", 2, 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("ngModelChange", function DatePickerComponent_Template_input_ngModelChange_2_listener($event) { return ctx.modelDate = $event; })("dateSelect", function DatePickerComponent_Template_input_dateSelect_2_listener() { return ctx.changePropertyValue(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "div", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "button", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function DatePickerComponent_Template_button_click_5_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r1); const _r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](3); return _r0.toggle(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "svg", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](7, "path", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](8, "path", 8);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("minDate", ctx.minDateRange)("startDate", ctx.setStartDate)("maxDate", ctx.maxDateRange)("ngModel", ctx.modelDate)("value", ctx.dateValue);
    } }, directives: [_ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbInputDatepicker"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["DefaultValueAccessor"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgModel"]], styles: [".form-group[_ngcontent-%COMP%] {\n  margin-bottom: 0rem !important;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvZGF0ZS1waWNrZXIvZGF0ZS1waWNrZXIuY29tcG9uZW50LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFBWSw4QkFBQTtBQUVaIiwiZmlsZSI6InNyYy9hcHAvZGF0ZS1waWNrZXIvZGF0ZS1waWNrZXIuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyIuZm9ybS1ncm91cHttYXJnaW4tYm90dG9tOiAwcmVtICFpbXBvcnRhbnQ7fSJdfQ== */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DatePickerComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-date-picker',
                templateUrl: './date-picker.component.html',
                styleUrls: ['./date-picker.component.scss'],
                providers: [_ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbInputDatepickerConfig"]]
            }]
    }], function () { return [{ type: _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbInputDatepickerConfig"] }, { type: _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_1__["NgbCalendar"] }]; }, { popoverText: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"],
            args: ['popover']
        }], startValue: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"],
            args: ['startValue']
        }], minDateRange: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"],
            args: ['minDate']
        }], maxDateRange: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"],
            args: ['maxDate']
        }], valueSelected: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"],
            args: ['rangeTo']
        }, {
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"],
            args: ['valueSelected']
        }] }); })();


/***/ }),

/***/ "./src/app/declaration/declaration.component.ts":
/*!******************************************************!*\
  !*** ./src/app/declaration/declaration.component.ts ***!
  \******************************************************/
/*! exports provided: DeclarationComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DeclarationComponent", function() { return DeclarationComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../main-header/main-header.component */ "./src/app/main-header/main-header.component.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");




const _c0 = function () { return [""]; };
class DeclarationComponent {
    constructor() { }
    ngOnInit() {
    }
}
DeclarationComponent.ɵfac = function DeclarationComponent_Factory(t) { return new (t || DeclarationComponent)(); };
DeclarationComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: DeclarationComponent, selectors: [["app-declaration"]], decls: 92, vars: 2, consts: [[1, "subTitle", "px-3", "mb-3"], [1, "fluid-container", "d-flex", "flex-wrap", "justify-content-start"], ["role", "link", "aria-label", "Powr\u00F3t do ekranu g\u0142\u00F3wnego", 1, "arrow-back", 3, "routerLink"], ["xmlns", "http://www.w3.org/2000/svg", "width", "18", "height", "18", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-chevron-left"], ["fill-rule", "evenodd", "d", "M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"], [1, "title"], [1, "container", "table-container", 2, "margin-top", "2rem"], [2, "padding", "1rem 0"], ["id", "dec"], ["id", "a11y-wstep"], ["id", "a11y-podmiot"], ["id", "a11y-url", "href", "https://www.gov.pl/web/sprawiedliwosc"], ["id", "a11y-data-publikacji"], ["id", "a11y-data-aktualizacja"], ["id", "a11y-status"], ["id", "list"], ["id", "a11y-data-soprzadzenie"], ["id", "a11y-kontakt"], ["id", "a11y-email"], ["href", "mailto:dostepnosc_cyfrowa@ms.gov.pl"], ["id", "a11y-telefon"], ["id", "a11t-procedura"], ["href", "https://www.rpo.gov.pl/content/jak-zglosic-sie-do-rzecznika-praw-obywatelskich"], ["id", "a11y-architektura"], ["id", "list2"]], template: function DeclarationComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "main-header");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "a", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "svg", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "path", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6, " Wstecz ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceHTML"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](8, " Deklaracja dost\u0119pno\u015Bci ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "div", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "article", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "h2");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](12, "Deklaracja dost\u0119pno\u015Bci Ministerstwa Sprawiedliwo\u015Bci");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "section");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "div", 8);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "p", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "span", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](17, "Ministerstwo Sprawiedliwo\u015Bci");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](18, " zobowi\u0105zuje si\u0119 zapewni\u0107 dost\u0119pno\u015B\u0107 swojej strony internetowej zgodnie z przepisami ustawy z dnia 4 kwietnia 2019 r. o dost\u0119pno\u015Bci cyfrowej stron internetowych i aplikacji mobilnych podmiot\u00F3w publicznych. O\u015Bwiadczenie w sprawie dost\u0119pno\u015Bci ma zastosowanie do strony internetowej ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "a", 11);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "Ministerstwa Sprawiedliwo\u015Bci.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](21, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](23, "Data publikacji strony internetowej: ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](24, "span", 12);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](25, "2019.08.05");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](26, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](27, "Data ostatniej du\u017Cej aktualizacji: ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](28, "span", 13);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](29, "2019.08.05");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](30, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](31, "p", 14);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](32, " Strona internetowa jest cz\u0119\u015Bciowo zgodna z ustaw\u0105 z dnia 4 kwietnia 2019 r. o dost\u0119pno\u015Bci cyfrowej stron internetowych i aplikacji mobilnych podmiot\u00F3w publicznych z powodu niezgodno\u015Bci lub wy\u0142\u0105cze\u0144 wymienionych poni\u017Cej:");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](33, "ol", 15);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](34, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](35, "Mog\u0105 zdarzy\u0107 si\u0119 sytuacje, \u017Ce pomimo stara\u0144 redaktor\u00F3w serwisu, niekt\u00F3re dokumenty opublikowane na stronie s\u0105 niedost\u0119pne z uwagi na fakt, \u017Ce: ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](36, "ul", 15);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](37, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](38, "pochodz\u0105 z r\u00F3\u017Cnych \u017Ar\u00F3de\u0142;");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](39, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](40, "zosta\u0142y opublikowane w oparciu o zasady przyj\u0119te w innej instytucji;");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](41, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](42, "s\u0105 bardzo obszerne, a ich wytworzenie odbywa\u0142o si\u0119 w kilku kom\u00F3rkach organizacyjnych, co uniemo\u017Cliwia\u0142o wp\u0142yw na ich docelow\u0105 tre\u015B\u0107 oraz kszta\u0142t;");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](43, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](44, "zosta\u0142y opublikowane przed wej\u015Bciem w \u017Cycie ustawy o dost\u0119pno\u015Bci cyfrowej.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](45, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](46, "Mo\u017Cliwe jest, \u017Ce niekt\u00F3re filmy i grafiki zamieszczone w serwisie \u2013 opublikowane przed wej\u015Bciem w \u017Cycie ustawy o dost\u0119pno\u015Bci cyfrowej \u2013 mog\u0105 nie posiada\u0107 napis\u00F3w lub innych wymaganych element\u00F3w zapewniaj\u0105cych dost\u0119pno\u015B\u0107.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](47, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](48, "Niekt\u00F3re zdj\u0119cia mog\u0105 nie zawiera\u0107 poprawnych opis\u00F3w alternatywnych.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](49, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](50, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](51, "O\u015Bwiadczenie sporz\u0105dzono dnia: ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](52, "span", 16);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](53, "2021-05-17.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](54, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](55, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](56, "Deklaracj\u0119 sporz\u0105dzono na podstawie samooceny przeprowadzonej przez podmiot publiczny.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](57, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](58, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](59, "Na stronie internetowej mo\u017Cna korzysta\u0107 ze standardowych skr\u00F3t\u00F3w klawiaturowych.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](60, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](61, "h3", 17);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](62, "Informacje zwrotne i dane kontaktowe");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](63, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](64, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](65, "W przypadku problem\u00F3w z dost\u0119pno\u015Bci\u0105 strony internetowej prosimy o kontakt pod adresem mailowym ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](66, "span", 18);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](67, "a", 19);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](68, "dostepnosc_cyfrowa@ms.gov.pl");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](69, " Kontaktowa\u0107 mo\u017Cna si\u0119 tak\u017Ce dzwoni\u0105c na numer telefonu ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](70, "span", 20);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](71, "+48 22 52 12 888.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](72, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](73, "p");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](74, "T\u0105 sam\u0105 drog\u0105 mo\u017Cna sk\u0142ada\u0107 wnioski o udost\u0119pnienie informacji niedost\u0119pnej oraz sk\u0142ada\u0107 skargi na brak zapewnienia dost\u0119pno\u015Bci.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](75, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](76, "p", 21);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](77, "Ka\u017Cdy ma prawo do wyst\u0105pienia z \u017C\u0105daniem zapewnienia dost\u0119pno\u015Bci cyfrowej strony internetowej, aplikacji mobilnej lub jakiego\u015B ich elementu. Mo\u017Cna tak\u017Ce za\u017C\u0105da\u0107 udost\u0119pnienia informacji za pomoc\u0105 alternatywnego sposobu dost\u0119pu, na przyk\u0142ad przez odczytanie niedost\u0119pnego cyfrowo dokumentu, opisanie zawarto\u015Bci filmu bez audiodeskrypcji itp. \u017B\u0105danie powinno zawiera\u0107 dane osoby zg\u0142aszaj\u0105cej \u017C\u0105danie, wskazanie, o kt\u00F3r\u0105 stron\u0119 internetow\u0105 lub aplikacj\u0119 mobiln\u0105 chodzi oraz spos\u00F3b kontaktu. Je\u017Celi osoba \u017C\u0105daj\u0105ca zg\u0142asza potrzeb\u0119 otrzymania informacji za pomoc\u0105 alternatywnego sposobu dost\u0119pu, powinna tak\u017Ce okre\u015Bli\u0107 dogodny dla niej spos\u00F3b przedstawienia tej informacji. Podmiot publiczny powinien zrealizowa\u0107 \u017C\u0105danie niezw\u0142ocznie, nie p\u00F3\u017Aniej ni\u017C w ci\u0105gu 7 dni od dnia wyst\u0105pienia z \u017C\u0105daniem. Je\u017Celi dotrzymanie tego terminu nie jest mo\u017Cliwe, podmiot publiczny niezw\u0142ocznie informuje o tym wnosz\u0105cego \u017C\u0105danie, kiedy realizacja \u017C\u0105dania b\u0119dzie mo\u017Cliwa, przy czym termin ten nie mo\u017Ce by\u0107 d\u0142u\u017Cszy ni\u017C 2 miesi\u0105ce od dnia wyst\u0105pienia z \u017C\u0105daniem. Je\u017Celi zapewnienie dost\u0119pno\u015Bci cyfrowej nie jest mo\u017Cliwe, podmiot publiczny mo\u017Ce zaproponowa\u0107 alternatywny spos\u00F3b dost\u0119pu do informacji. W przypadku, gdy podmiot publiczny odm\u00F3wi realizacji \u017C\u0105dania zapewnienia dost\u0119pno\u015Bci lub alternatywnego sposobu dost\u0119pu do informacji, wnosz\u0105cy \u017C\u0105danie mo\u017Cne z\u0142o\u017Cy\u0107 skarg\u0119 w sprawie zapewniana dost\u0119pno\u015Bci cyfrowej strony internetowej, aplikacji mobilnej lub elementu strony internetowej, lub aplikacji mobilnej. ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](78, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](79, " Po wyczerpaniu wszystkich mo\u017Cliwo\u015Bci skarg\u0119 mo\u017Cna przes\u0142a\u0107 tak\u017Ce do ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](80, "a", 22);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](81, "Rzecznika Praw Obywatelskich.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](82, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](83, "h3", 23);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](84, "Dost\u0119pno\u015B\u0107 architektoniczna");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](85, "br");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](86, " Do wszystkich obiekt\u00F3w umo\u017Cliwiony jest wjazd osobom na w\u00F3zkach inwalidzkich przy pomocy wind zewn\u0119trznych (Al. Ujazdowskie 11, ul. Czerniakowska 100) lub podjazdu (ul. Chopina 1, ul. Zwyci\u0119zc\u00F3w 34). Wszystkie obiekty posiadaj\u0105 windy osobowe, umo\u017Cliwiaj\u0105ce poruszanie si\u0119 i dost\u0119p na ka\u017Cde pi\u0119tro budynk\u00F3w, gdy\u017C windy te zosta\u0142y wyposa\u017Cone w przyciski steruj\u0105ce, umo\u017Cliwiaj\u0105ce odczyt osobom niewidomym i niedowidz\u0105cym, jak r\u00F3wnie\u017C sygnalizacj\u0119 d\u017Awi\u0119kow\u0105 informuj\u0105c\u0105 o pozycji windy. Zlikwidowane zosta\u0142y bariery w postaci prog\u00F3w i r\u00F3\u017Cnic w poziomie pod\u0142\u00F3g pokoi i korytarzy. Ponadto wszystkie budynki Ministerstwa, kt\u00F3re nie s\u0105 zabytkami, posiadaj\u0105 toalety dostosowane dla os\u00F3b niepe\u0142nosprawnych. W budynkach, kt\u00F3re s\u0105 pod opiek\u0105 konserwatora zabytk\u00F3w, tj.: ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](87, "ul", 24);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](88, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](89, "w budynku przy Al. R\u00F3\u017C 2 (wpisanym do rejestru zabytk\u00F3w pod nr 595 \u2013 decyzja z dn. 01.07.1965r.), w 2016r zako\u0144czono remont kapitalny, w ramach kt\u00F3rego uwzgl\u0119dniono wymagania os\u00F3b niepe\u0142nosprawnych,");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](90, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](91, "w budynku przy Al. Ujazdowskich 19 (wpisanym do rejestru zabytk\u00F3w pod nr 749 \u2013 decyzja z dn. 01.07.1965r.) zaplanowano na kolejne lata remont generalny (jednak\u017Ce z uwagi na wniesione do przedmiotowego obiektu roszczenia w\u0142asno\u015Bciowe, termin rozpocz\u0119cia prac jest nieznany), gdzie uwzgl\u0119dniono przepisy w zakresie dostosowania do potrzeb os\u00F3b niepe\u0142nosprawnych og\u00F3lnodost\u0119pnych cz\u0119\u015Bci budynku, wynikaj\u0105ce z uchwa\u0142y Sejmu Rzeczypospolitej Polskiej z dnia 01.08.1997r \u2013 Karta Praw Os\u00F3b Niepe\u0142nosprawnych.");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction0"](1, _c0));
    } }, directives: [_main_header_main_header_component__WEBPACK_IMPORTED_MODULE_1__["MainHeaderComponent"], _angular_router__WEBPACK_IMPORTED_MODULE_2__["RouterLinkWithHref"]], styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJzcmMvYXBwL2RlY2xhcmF0aW9uL2RlY2xhcmF0aW9uLmNvbXBvbmVudC5zY3NzIn0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](DeclarationComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'app-declaration',
                templateUrl: './declaration.component.html',
                styleUrls: ['./declaration.component.scss']
            }]
    }], function () { return []; }, null); })();


/***/ }),

/***/ "./src/app/list-by-year/list-by-year.component.ts":
/*!********************************************************!*\
  !*** ./src/app/list-by-year/list-by-year.component.ts ***!
  \********************************************************/
/*! exports provided: ListByYearComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ListByYearComponent", function() { return ListByYearComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
/* harmony import */ var _services_api_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./../services/api.service */ "./src/app/services/api.service.ts");
/* harmony import */ var _services_state_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./../services/state.service */ "./src/app/services/state.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/http.js");
/* harmony import */ var _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../main-header/main-header.component */ "./src/app/main-header/main-header.component.ts");
/* harmony import */ var _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../shared/fullsize-loader/fullsize-loader.component */ "./src/app/shared/fullsize-loader/fullsize-loader.component.ts");
/* harmony import */ var _services_format_bytes_pipe__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ../services/format-bytes.pipe */ "./src/app/services/format-bytes.pipe.ts");












function ListByYearComponent_fullsize_loader_0_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "fullsize-loader");
} }
function ListByYearComponent_div_8_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceHTML"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 11);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " Pobierz monitor ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function ListByYearComponent_div_9_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceHTML"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 11);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, " Pobierz monitor - Archiwum ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function ListByYearComponent_form_11_option_5_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "option", 17);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const year_r6 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngValue", year_r6);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", year_r6, " ");
} }
function ListByYearComponent_form_11_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "form", 12);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 13);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "label", 14);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](3, "Wybierz rok");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "select", 15);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](5, ListByYearComponent_form_11_option_5_Template, 2, 2, "option", 16);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("formGroup", ctx_r3.tableForm);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("compareWith", ctx_r3.compareByID);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx_r3.years);
} }
function ListByYearComponent_div_13_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 18);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 19);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](5, "date");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "div", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipe"](8, "formatBytes");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "div", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "a", 21);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](11, "svg", 22);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "path", 23);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](13, "path", 24);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, " Pobierz");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const msigRow_r7 = ctx.$implicit;
    const ctx_r4 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", msigRow_r7.monitorNumber, "");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind2"](5, 5, msigRow_r7.date, "yyyy-LL-dd"));
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpipeBind1"](8, 8, msigRow_r7 == null ? null : msigRow_r7.dataLenght), "");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate2"]("href", "", ctx_r4.apiURL, "/Monitor/Download?id=", msigRow_r7.id, "&fileId=true", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵsanitizeUrl"]);
} }
const _c0 = function () { return [""]; };
class ListByYearComponent {
    constructor(fb, api, state, location, route, document, http) {
        this.fb = fb;
        this.api = api;
        this.state = state;
        this.location = location;
        this.route = route;
        this.document = document;
        this.http = http;
        this.fullsizeLoader = false;
        this.alertWarning = false;
        this.hideNext = true;
        this.years = [];
        this.tryTofive = 0;
        this.archives = false;
    }
    ngOnInit() {
        this.generateYears();
        this.state.url$.subscribe({
            next: url => {
                this.apiURL = url;
                if (this.apiURL) {
                    this.getData();
                }
            }
        });
    }
    ngOnDestroy() {
        if (this.dataSubscription) {
            this.dataSubscription.unsubscribe();
        }
        // if(this.urlSubscription) {
        //   this.urlSubscription.unsubscribe();
        // }
    }
    urlState() {
        return new Promise((resolve, reject) => {
            this.state.url$.subscribe({
                next: url => {
                    this.apiURL = url;
                    // console.log(this.apiURL)
                    if (this.apiURL == undefined) {
                        reject('error');
                    }
                    else {
                        resolve('done');
                    }
                }
            });
        });
    }
    fromApp() {
        return new Promise((resolve, reject) => {
            this.state.url$.subscribe({
                next: url => {
                    this.apiURL = url;
                    // console.log(this.apiURL)
                    if (this.apiURL == undefined) {
                        reject('error');
                    }
                    else {
                        resolve('done');
                    }
                }
            });
        });
    }
    getData() {
        this.route.params.subscribe(res => {
            if (res.year) {
                this.currentYear = res.year;
                this.tableForm = this.tableFormInit();
                this.monitorByYear(this.currentYear);
                this.yearChanged();
            }
        });
    }
    tableFormInit() {
        return this.fb.group({
            year: [this.currentYear],
        });
    }
    yearChanged() {
        this.tableForm.get('year').valueChanges.subscribe({
            next: value => {
                this.currentYear = value;
                this.monitorByYear(value);
                this.location.go(`/pobieranie-monitora/${this.currentYear}`);
            }
        });
    }
    getApiUrl() {
        let url = `${document.location.origin}/`; //document.location.href;
        this.http.get(`${url}home/getapiurl`, { responseType: 'text' }).subscribe({
            next: res => {
                this.apiURL = res;
                this.state.shareUrl(this.apiURL);
            },
            error: err => {
                console.log(err);
            }
        });
    }
    generateYears() {
        let yearToday = new Date().getFullYear();
        let startYear = 1996;
        while (startYear < yearToday) {
            this.years.length === 0 ? startYear : startYear = startYear + 1;
            let year = startYear;
            this.years.push(year.toString());
        }
    }
    monitorByYear(year) {
        this.fullsizeLoader = true;
        if (year < 2001) {
            this.archives = true;
        }
        else {
            this.archives = false;
        }
        this.dataSubscription = this.api.getMonitorByYear(year).subscribe({
            next: res => {
                this.msigList = res;
                this.fullsizeLoader = false;
                if (this.msigList.length == 0) {
                    this.state.shareAlertBody([{
                            status: 'info',
                            message: 'Brak wyników. Zmień rok.',
                            alwaysVisible: false
                        }]);
                }
            },
            error: err => {
                console.log(err);
                this.state.shareAlertBody([{
                        status: 'danger',
                        message: 'Wystąpił bład.',
                        alwaysVisible: false
                    }]);
                this.tryTofive = 0;
                this.fullsizeLoader = false;
            }
        });
    }
    downloadFile(data) {
        const url = window.URL.createObjectURL(data);
        window.open(url);
    }
    compareByID(itemOne, itemTwo) {
        return itemOne == itemTwo;
    }
}
ListByYearComponent.ɵfac = function ListByYearComponent_Factory(t) { return new (t || ListByYearComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormBuilder"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_api_service__WEBPACK_IMPORTED_MODULE_3__["ApiService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_state_service__WEBPACK_IMPORTED_MODULE_4__["StateService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_common__WEBPACK_IMPORTED_MODULE_1__["Location"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_router__WEBPACK_IMPORTED_MODULE_5__["ActivatedRoute"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_common__WEBPACK_IMPORTED_MODULE_1__["DOCUMENT"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_6__["HttpClient"])); };
ListByYearComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: ListByYearComponent, selectors: [["table-list"]], decls: 14, vars: 7, consts: [[4, "ngIf"], [1, "subTitle", "px-3", "mb-3"], [1, "fluid-container", "d-flex", "flex-wrap", "justify-content-start"], ["role", "link", "aria-label", "Powr\u00F3t do ekranu g\u0142\u00F3wnego", 1, "arrow-back", 3, "routerLink"], ["xmlns", "http://www.w3.org/2000/svg", "width", "18", "height", "18", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-chevron-left"], ["fill-rule", "evenodd", "d", "M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"], ["class", "title", 4, "ngIf"], [1, "container", "table-container", 2, "margin-top", "75px"], [3, "formGroup", 4, "ngIf"], [1, "row"], ["class", "col-sm-6 col-md-3 col-lg-2 monitor-tile", 4, "ngFor", "ngForOf"], [1, "title"], [3, "formGroup"], [1, "mb-3"], ["for", "formyear", 1, "form-label"], ["id", "formyear", "aria-label", "Wybierz rok monitora", "formControlName", "year", 1, "form-control", 3, "compareWith"], [3, "ngValue", 4, "ngFor", "ngForOf"], [3, "ngValue"], [1, "col-sm-6", "col-md-3", "col-lg-2", "monitor-tile"], [1, "monitor-number"], [1, ""], ["type", "button", "download", "", 1, "btn", "btn-link", "table-action_link", 3, "href"], ["xmlns", "http://www.w3.org/2000/svg", "width", "16", "height", "16", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-download"], ["d", "M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"], ["d", "M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"]], template: function ListByYearComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](0, ListByYearComponent_fullsize_loader_0_Template, 1, 0, "fullsize-loader", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "main-header");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "a", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "svg", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](6, "path", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, " Wstecz ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](8, ListByYearComponent_div_8_Template, 2, 0, "div", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](9, ListByYearComponent_div_9_Template, 2, 0, "div", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceHTML"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "div", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](11, ListByYearComponent_form_11_Template, 6, 3, "form", 8);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "div", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](13, ListByYearComponent_div_13_Template, 15, 10, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.fullsizeLoader);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction0"](6, _c0));
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", !ctx.archives);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.archives);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.tableForm);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.msigList);
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["NgIf"], _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_7__["MainHeaderComponent"], _angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterLinkWithHref"], _angular_common__WEBPACK_IMPORTED_MODULE_1__["NgForOf"], _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_8__["FullsizeLoaderComponent"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["ɵangular_packages_forms_forms_y"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgControlStatusGroup"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormGroupDirective"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["SelectControlValueAccessor"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormControlName"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["NgSelectOption"], _angular_forms__WEBPACK_IMPORTED_MODULE_2__["ɵangular_packages_forms_forms_x"]], pipes: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["DatePipe"], _services_format_bytes_pipe__WEBPACK_IMPORTED_MODULE_9__["FormatBytesPipe"]], styles: [".center-content[_ngcontent-%COMP%] {\n  padding: 4px 2px !important;\n}\n.modal-title_sub[_ngcontent-%COMP%] {\n  font-size: 1rem;\n  font-weight: 400;\n}\n.modal-title_sub[_ngcontent-%COMP%]   span[_ngcontent-%COMP%] {\n  font-weight: 600;\n}\n.pages[_ngcontent-%COMP%] {\n  color: #003366;\n}\n.pages[_ngcontent-%COMP%]   span[_ngcontent-%COMP%] {\n  font-weight: 500;\n}\n.btn.prev[_ngcontent-%COMP%], .btn.next[_ngcontent-%COMP%] {\n  color: #003366;\n}\n.btn.prev[_ngcontent-%COMP%]:hover, .btn.next[_ngcontent-%COMP%]:hover {\n  text-decoration: underline;\n}\n.monitor-tile[_ngcontent-%COMP%] {\n  text-align: center;\n  border-bottom: 1px solid #d1d1d1;\n  padding: 8px 0px;\n}\n.monitor-tile[_ngcontent-%COMP%]   .monitor-number[_ngcontent-%COMP%] {\n  font-weight: bold;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9zdHlsZXMvY29sb3JzLnNjc3MiLCJzcmMvYXBwL2xpc3QtYnkteWVhci9saXN0LWJ5LXllYXIuY29tcG9uZW50LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUEsZ0JBQUE7QUNFQTtFQUNJLDJCQUFBO0FBQUo7QUFRQTtFQUNJLGVBQUE7RUFDQSxnQkFBQTtBQUxKO0FBT0k7RUFDSSxnQkFBQTtBQUxSO0FBVUE7RUFDSSxjRFpXO0FDS2Y7QUFTSTtFQUNJLGdCQUFBO0FBUFI7QUFZQTtFQUVJLGNEdEJXO0FDWWY7QUFZSTtFQUNJLDBCQUFBO0FBVlI7QUFhQTtFQUVJLGtCQUFBO0VBQ0EsZ0NBQUE7RUFDQSxnQkFBQTtBQVhKO0FBYUk7RUFDSSxpQkFBQTtBQVhSIiwiZmlsZSI6InNyYy9hcHAvbGlzdC1ieS15ZWFyL2xpc3QtYnkteWVhci5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIi8qIGJhc2UgY29sb3JzICovXHJcblxyXG4kY29sb3JfZ3JleV8xOiAjMGQwZDBkOyBcclxuJGNvbG9yX2dyZXlfMjogIzMzMzMzMzsgXHJcbiRjb2xvcl9ncmV5XzM6ICM0ZDRkNGQ7IFxyXG4kY29sb3JfZ3JleV80OiAjNjY2O1xyXG4kY29sb3JfZ3JleV81OiAjYjJiMmIyO1xyXG4kY29sb3JfZ3JleV82OiAjZDlkOWQ5O1xyXG4kY29sb3JfZ3JleV82OiAjZjVmNWY1OyAgXHJcblxyXG4kY29sb3JfYmx1ZV8xOiAjMDAzMzY2OyBcclxuJGNvbG9yX2JsdWVfMjogIzAwNDI4NDsgXHJcbiRjb2xvcl9ibHVlXzM6ICMwMDUyYTU7IFxyXG4kY29sb3JfYmx1ZV80OiAjOTljY2ZmOyBcclxuJGNvbG9yX2JsdWVfNTogI2Y1ZmFmZjsgXHJcblxyXG4kY29sb3JfZ3JlZW5fMTogIzE4MzUxODsgXHJcbiRjb2xvcl9ncmVlbl8yOiAjM2E4MjNhOyBcclxuJGNvbG9yX2dyZWVuXzM6ICNiOWRmYjk7IFxyXG4kY29sb3JfZ3JlZW5fNDogI2VkZjdlZDsgXHJcblxyXG4kY29sb3JfcmVkXzE6ICM2NjAwMGE7IFxyXG4kY29sb3JfcmVkXzI6ICNkNTIzM2Y7Ly8jYTgwMDExOyBcclxuJGNvbG9yX3JlZF8zOiAjZmZiMmJhOyBcclxuJGNvbG9yX3JlZF80OiAjZmZmMGYxO1xyXG5cclxuJGNvbG9yX2luZl8xOiAjMDQ0MzYyOyBcclxuJGNvbG9yX2luZl8yOiAjMDY1YTg0OyBcclxuJGNvbG9yX2luZl8zOiAjYjVlNWZjOyBcclxuJGNvbG9yX2luZl80OiAjZjVmYmZmO1xyXG5cclxuJGNvbG9yX3dhcm5pbmdfMTogIzU3NDEwMDsgXHJcbiRjb2xvcl93YXJuaW5nXzI6ICNlNWFjMDA7IFxyXG4kY29sb3Jfd2FybmluZ18zOiAjZmZkZjgwOyBcclxuJGNvbG9yX3dhcm5pbmdfNDogI2ZmZjllNTtcclxuXHJcbiRjb250cmFzdF9iYWNrZ3JvdW51ZDogIzBkMGQwZDtcclxuJGNvbnRyYXN0X2ZvbnQ6ICNmZmY3MDA7XHJcbiRjb250cmFzdF9saW5rOiAjZmZmO1xyXG5cclxuIiwiQGltcG9ydCBcIi4vLi4vLi4vc3R5bGVzL2NvbG9ycy5zY3NzXCI7XHJcblxyXG4uY2VudGVyLWNvbnRlbnQge1xyXG4gICAgcGFkZGluZzogNHB4IDJweCAhaW1wb3J0YW50O1xyXG59XHJcblxyXG5cclxuLnRhYmxlLWFjdGlvbl9saW5re1xyXG4gICAgLy8gZm9udC1zaXplOiAxNHB4O1xyXG59XHJcblxyXG4ubW9kYWwtdGl0bGVfc3ViIHtcclxuICAgIGZvbnQtc2l6ZTogMXJlbTtcclxuICAgIGZvbnQtd2VpZ2h0OiA0MDA7XHJcblxyXG4gICAgc3BhbiB7XHJcbiAgICAgICAgZm9udC13ZWlnaHQ6IDYwMDtcclxuICAgIH1cclxufVxyXG5cclxuXHJcbi5wYWdlc3tcclxuICAgIGNvbG9yOiAkY29sb3JfYmx1ZV8xO1xyXG5cclxuICAgIHNwYW4ge1xyXG4gICAgICAgIGZvbnQtd2VpZ2h0OjUwMDtcclxuICAgICAgICAvLyBjb2xvcjogJGNvbG9yX2JsdWVfMTtcclxuICAgIH1cclxufVxyXG5cclxuLmJ0bi5wcmV2LCAuYnRuLm5leHQge1xyXG5cclxuICAgIGNvbG9yOiAkY29sb3JfYmx1ZV8xO1xyXG5cclxuICAgICY6aG92ZXIge1xyXG4gICAgICAgIHRleHQtZGVjb3JhdGlvbjogdW5kZXJsaW5lO1xyXG4gICAgfVxyXG59XHJcbi5tb25pdG9yLXRpbGUge1xyXG5cclxuICAgIHRleHQtYWxpZ246IGNlbnRlcjtcclxuICAgIGJvcmRlci1ib3R0b206IDFweCBzb2xpZCAjZDFkMWQxOyAgICBcclxuICAgIHBhZGRpbmc6IDhweCAwcHg7XHJcblxyXG4gICAgLm1vbml0b3ItbnVtYmVye1xyXG4gICAgICAgIGZvbnQtd2VpZ2h0OmJvbGQ7XHJcbiAgICAgICBcclxuICAgIH1cclxuXHJcbn1cclxuIl19 */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](ListByYearComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'table-list',
                templateUrl: './list-by-year.component.html',
                styleUrls: ['./list-by-year.component.scss']
            }]
    }], function () { return [{ type: _angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormBuilder"] }, { type: _services_api_service__WEBPACK_IMPORTED_MODULE_3__["ApiService"] }, { type: _services_state_service__WEBPACK_IMPORTED_MODULE_4__["StateService"] }, { type: _angular_common__WEBPACK_IMPORTED_MODULE_1__["Location"] }, { type: _angular_router__WEBPACK_IMPORTED_MODULE_5__["ActivatedRoute"] }, { type: undefined, decorators: [{
                type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Inject"],
                args: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["DOCUMENT"]]
            }] }, { type: _angular_common_http__WEBPACK_IMPORTED_MODULE_6__["HttpClient"] }]; }, null); })();


/***/ }),

/***/ "./src/app/main-header/main-header.component.ts":
/*!******************************************************!*\
  !*** ./src/app/main-header/main-header.component.ts ***!
  \******************************************************/
/*! exports provided: MainHeaderComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MainHeaderComponent", function() { return MainHeaderComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _services_state_service__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./../services/state.service */ "./src/app/services/state.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");






const _c0 = [[["", 8, "subtitle"]]];
const _c1 = function () { return [""]; };
const _c2 = function (a0, a1) { return { "bi-eye": a0, "bi-eye-fill": a1 }; };
const _c3 = [".subTitle"];
class MainHeaderComponent {
    constructor(state, document) {
        this.state = state;
        this.document = document;
        this.contrastStatus = false;
        this.accessibilityObj = {
            contrast: false,
            fontSizeNormal: true,
            fontSizeBigger: false,
            fontSizeBigest: false,
        };
    }
    ngOnInit() {
        this.state.accessibility$.subscribe({
            next: res => {
                this.contrastStatus = res === null || res === void 0 ? void 0 : res.contrast;
            }
        });
    }
    contrast() {
        this.contrastStatus = this.contrastStatus ? false : true;
        this.accessibilityObj.contrast = this.contrastStatus;
        this.state.shareAccessibility(this.accessibilityObj);
        this.document.body.classList.toggle('msig-contrast', this.contrastStatus);
    }
    changefontSize(size) {
        let htmlTag = this.document.querySelector('HTML');
        switch (size) {
            case "normal":
                this.accessibilityObj.fontSizeNormal = true;
                this.accessibilityObj.fontSizeBigest = false;
                this.accessibilityObj.fontSizeBigger = false;
                htmlTag.style.fontSize = '16px';
                break;
            case "bigger":
                this.accessibilityObj.fontSizeNormal = false;
                this.accessibilityObj.fontSizeBigest = false;
                this.accessibilityObj.fontSizeBigger = true;
                htmlTag.style.fontSize = '18px';
                break;
            case "bigest":
                this.accessibilityObj.fontSizeNormal = false;
                this.accessibilityObj.fontSizeBigest = true;
                this.accessibilityObj.fontSizeBigger = false;
                htmlTag.style.fontSize = '20px';
                break;
            default:
                this.accessibilityObj.fontSizeNormal = true;
                this.accessibilityObj.fontSizeBigest = false;
                this.accessibilityObj.fontSizeBigger = false;
                htmlTag.style.fontSize = '16px';
                break;
        }
        this.state.shareAccessibility(this.accessibilityObj);
    }
}
MainHeaderComponent.ɵfac = function MainHeaderComponent_Factory(t) { return new (t || MainHeaderComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_state_service__WEBPACK_IMPORTED_MODULE_2__["StateService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_common__WEBPACK_IMPORTED_MODULE_1__["DOCUMENT"])); };
MainHeaderComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: MainHeaderComponent, selectors: [["main-header"]], ngContentSelectors: _c3, decls: 22, vars: 6, consts: [[1, "px-3", "py-2", "bg-white"], [1, "fluid-container"], [1, "d-flex", "flex-wrap", "align-items-center", "justify-content-center", "justify-content-lg-start", 2, "justify-content", "start !important"], ["aria-label", "przejd\u017A do g\u0142\u00F3wnego widoku", "alt", "logo Ministerstwa Sprawiedliwo\u015Bci", 1, "gov-pl", 3, "routerLink"], [1, "portal-name"], [1, "accessibility"], ["aria-label", "Wersja o podwy\u017Cszonym kontra\u015Bcie", "alt", "Zmie\u0144 kontrast strony", "tabindex", "0", 3, "keyup.enter", "click"], [1, "bi", 2, "font-size", "2rem", 3, "ngClass"], [2, "font-size", "2rem"], ["aria-label", "Zmiana wielko\u015Bci czcionki na najwi\u0119ksza", "alt", "Czcionka o najwi\u0119kszej wielko\u015Bci", "tabindex", "0", 3, "click", "keyup.enter"], [2, "font-size", "1.6rem"], ["aria-label", "Zmiana wielko\u015Bci czcionki na \u015Bredni\u0105", "alt", "Czcionka o \u015Bredniej wielko\u015Bci", "tabindex", "0", 3, "click", "keyup.enter"], [2, "font-size", "1.2rem"], ["tabindex", "0", "aria-label", "Zmie\u0144 wielko\u015Bci czcionki na normaln\u0105", "alt", "Czcionka o normalnej wielko\u015Bci", 3, "click", "keyup.enter"]], template: function MainHeaderComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵprojectionDef"](_c0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "header");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "a", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "span", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](6, " Monitor S\u0105dowy i Gospodarczy ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](7, "div", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "ul");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "li");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "a", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function MainHeaderComponent_Template_a_keyup_enter_10_listener() { return ctx.contrast(); })("click", function MainHeaderComponent_Template_a_click_10_listener() { return ctx.contrast(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](11, "i", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "li", 8);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "a", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function MainHeaderComponent_Template_a_click_13_listener() { return ctx.changefontSize("bigest"); })("keyup.enter", function MainHeaderComponent_Template_a_keyup_enter_13_listener() { return ctx.changefontSize("bigest"); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, "A");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "li", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "a", 11);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function MainHeaderComponent_Template_a_click_16_listener() { return ctx.changefontSize("bigger"); })("keyup.enter", function MainHeaderComponent_Template_a_keyup_enter_16_listener() { return ctx.changefontSize("bigger"); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](17, "A");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "li", 12);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "a", 13);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function MainHeaderComponent_Template_a_click_19_listener() { return ctx.changefontSize("normal"); })("keyup.enter", function MainHeaderComponent_Template_a_keyup_enter_19_listener() { return ctx.changefontSize("normal"); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "A");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵprojection"](21);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction0"](2, _c1));
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngClass", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction2"](3, _c2, ctx.contrastStatus, !ctx.contrastStatus));
    } }, directives: [_angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterLinkWithHref"], _angular_common__WEBPACK_IMPORTED_MODULE_1__["NgClass"]], styles: [".gov-pl[_ngcontent-%COMP%] {\n  background-image: url('logo-ms.svg');\n  background-position: 0rem 0.1rem;\n  height: 3.7rem;\n  width: 13.2rem;\n  margin: 0;\n  box-shadow: none;\n  background-size: contain;\n  background-repeat: no-repeat;\n  margin-left: 6px;\n  margin-top: 3px;\n}\n\n.portal-name[_ngcontent-%COMP%] {\n  flex-grow: 1;\n  display: flex;\n  align-items: center;\n  font-size: 1.05rem;\n  letter-spacing: 0.4px;\n  font-weight: 600;\n  border-left: 2px solid #d5233f;\n  padding-left: 1.2rem;\n  margin-left: 1.2rem;\n  line-height: 3rem;\n}\n\n.accessibility[_ngcontent-%COMP%]   ul[_ngcontent-%COMP%] {\n  margin: 0px;\n}\n\n.accessibility[_ngcontent-%COMP%]   ul[_ngcontent-%COMP%]   li[_ngcontent-%COMP%] {\n  display: inline-block;\n  list-style: none;\n  margin: 0 2px;\n  padding: 8px 3px;\n  cursor: pointer;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvbWFpbi1oZWFkZXIvbWFpbi1oZWFkZXIuY29tcG9uZW50LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFDRSxvQ0FBQTtFQUNBLGdDQUFBO0VBRUEsY0FBQTtFQUNBLGNBQUE7RUFDQSxTQUFBO0VBQ0EsZ0JBQUE7RUFDQSx3QkFBQTtFQUNBLDRCQUFBO0VBQ0EsZ0JBQUE7RUFDQSxlQUFBO0FBQUY7O0FBR0E7RUFFSSxZQUFBO0VBQ0EsYUFBQTtFQUNBLG1CQUFBO0VBQ0Esa0JBQUE7RUFDQSxxQkFBQTtFQUNBLGdCQUFBO0VBQ0EsOEJBQUE7RUFDQSxvQkFBQTtFQUNBLG1CQUFBO0VBQ0EsaUJBQUE7QUFESjs7QUFNRTtFQUVFLFdBQUE7QUFKSjs7QUFNSTtFQUNFLHFCQUFBO0VBQ0EsZ0JBQUE7RUFDQSxhQUFBO0VBQ0EsZ0JBQUE7RUFDQSxlQUFBO0FBSk4iLCJmaWxlIjoic3JjL2FwcC9tYWluLWhlYWRlci9tYWluLWhlYWRlci5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIi5nb3YtcGwge1xyXG4gIGJhY2tncm91bmQtaW1hZ2U6IHVybCguLi8uLi9hc3NldHMvbG9nby1tcy5zdmcpO1xyXG4gIGJhY2tncm91bmQtcG9zaXRpb246IDByZW0gMC4xcmVtO1xyXG4gIC8vICAgYmFja2dyb3VuZC1zaXplOiAxNi4xNHJlbSA0cmVtO1xyXG4gIGhlaWdodDogMy43cmVtO1xyXG4gIHdpZHRoOiAxMy4ycmVtO1xyXG4gIG1hcmdpbjogMDtcclxuICBib3gtc2hhZG93OiBub25lO1xyXG4gIGJhY2tncm91bmQtc2l6ZTogY29udGFpbjtcclxuICBiYWNrZ3JvdW5kLXJlcGVhdDogbm8tcmVwZWF0O1xyXG4gIG1hcmdpbi1sZWZ0OiA2cHg7XHJcbiAgbWFyZ2luLXRvcDogM3B4O1xyXG59XHJcblxyXG4ucG9ydGFsLW5hbWUge1xyXG5cclxuICAgIGZsZXgtZ3JvdzogMTtcclxuICAgIGRpc3BsYXk6IGZsZXg7XHJcbiAgICBhbGlnbi1pdGVtczogY2VudGVyO1xyXG4gICAgZm9udC1zaXplOiAxLjA1cmVtO1xyXG4gICAgbGV0dGVyLXNwYWNpbmc6IDAuNHB4O1xyXG4gICAgZm9udC13ZWlnaHQ6IDYwMDtcclxuICAgIGJvcmRlci1sZWZ0OiAycHggc29saWQgI2Q1MjMzZjtcclxuICAgIHBhZGRpbmctbGVmdDogMS4ycmVtO1xyXG4gICAgbWFyZ2luLWxlZnQ6IDEuMnJlbTtcclxuICAgIGxpbmUtaGVpZ2h0OiAzcmVtO1xyXG5cclxufVxyXG5cclxuLmFjY2Vzc2liaWxpdHkge1xyXG4gIHVsIHsgXHJcblxyXG4gICAgbWFyZ2luOiAwcHg7XHJcblxyXG4gICAgbGkge1xyXG4gICAgICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XHJcbiAgICAgIGxpc3Qtc3R5bGU6IG5vbmU7XHJcbiAgICAgIG1hcmdpbjowIDJweDtcclxuICAgICAgcGFkZGluZzogOHB4IDNweDtcclxuICAgICAgY3Vyc29yOiBwb2ludGVyO1xyXG4gICAgfVxyXG4gIH1cclxufSJdfQ== */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](MainHeaderComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'main-header',
                templateUrl: './main-header.component.html',
                styleUrls: ['./main-header.component.scss']
            }]
    }], function () { return [{ type: _services_state_service__WEBPACK_IMPORTED_MODULE_2__["StateService"] }, { type: undefined, decorators: [{
                type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Inject"],
                args: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["DOCUMENT"]]
            }] }]; }, null); })();


/***/ }),

/***/ "./src/app/search-form/CheckNipValidator.ts":
/*!**************************************************!*\
  !*** ./src/app/search-form/CheckNipValidator.ts ***!
  \**************************************************/
/*! exports provided: CheckNipValidator */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CheckNipValidator", function() { return CheckNipValidator; });
class CheckNipValidator {
    static checkNip(control) {
        var _a;
        if (control.value) {
            let nip = (_a = control.value) === null || _a === void 0 ? void 0 : _a.toString();
            var nipWithoutDashes = nip.replace(/-/g, "");
            var reg = /^[0-9]{10}$/;
            if (reg.test(nipWithoutDashes) == false) {
                return null;
            }
            else {
                var digits = ("" + nipWithoutDashes).split("");
                var checksum = (6 * parseInt(digits[0]) + 5 * parseInt(digits[1]) + 7 * parseInt(digits[2]) + 2 * parseInt(digits[3]) + 3 * parseInt(digits[4]) + 4 * parseInt(digits[5]) + 5 * parseInt(digits[6]) + 6 * parseInt(digits[7]) + 7 * parseInt(digits[8])) % 11;
                console.log((parseInt(digits[9]) == checksum));
                return {
                    checkNip: (parseInt(digits[9]) == checksum)
                };
            }
            ;
        }
    }
}


/***/ }),

/***/ "./src/app/search-form/search-form.component.ts":
/*!******************************************************!*\
  !*** ./src/app/search-form/search-form.component.ts ***!
  \******************************************************/
/*! exports provided: SearchFormComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SearchFormComponent", function() { return SearchFormComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/__ivy_ngcc__/fesm2015/forms.js");
/* harmony import */ var _CheckNipValidator__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./CheckNipValidator */ "./src/app/search-form/CheckNipValidator.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
/* harmony import */ var _services_api_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./../services/api.service */ "./src/app/services/api.service.ts");
/* harmony import */ var _services_state_service__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./../services/state.service */ "./src/app/services/state.service.ts");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../main-header/main-header.component */ "./src/app/main-header/main-header.component.ts");
/* harmony import */ var ngx_mask__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ngx-mask */ "./node_modules/ngx-mask/__ivy_ngcc__/fesm2015/ngx-mask.js");
/* harmony import */ var _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @ng-bootstrap/ng-bootstrap */ "./node_modules/@ng-bootstrap/ng-bootstrap/__ivy_ngcc__/fesm2015/ng-bootstrap.js");
/* harmony import */ var _date_picker_date_picker_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ../date-picker/date-picker.component */ "./src/app/date-picker/date-picker.component.ts");
/* harmony import */ var _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../shared/fullsize-loader/fullsize-loader.component */ "./src/app/shared/fullsize-loader/fullsize-loader.component.ts");














function SearchFormComponent_fullsize_loader_0_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "fullsize-loader");
} }
function SearchFormComponent_ng_template_23_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "span", 38);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1, "Nieprawid\u0142owy numer NIP");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function SearchFormComponent_option_42_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "option", 39);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const base_r15 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("aria-label", base_r15.name);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngValue", base_r15.val);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", base_r15.name, " ");
} }
function SearchFormComponent_div_43_Template(rf, ctx) { if (rf & 1) {
    const _r18 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 10);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "label", 40);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "Sygnatura sprawy ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "span", 41, 42);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_div_43_Template_span_keyup_enter_3_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r18); const _r16 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](4); return _r16.open(); });
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "input", 43);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("autoClose", true);
} }
function SearchFormComponent_div_44_Template(rf, ctx) { if (rf & 1) {
    const _r21 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 10);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "label", 44);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "S\u0105d ");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "span", 45, 18);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_div_44_Template_span_keyup_enter_3_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r21); const _r19 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](4); return _r19.open(); });
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "input", 46);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("autoClose", true);
} }
function SearchFormComponent_div_45_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 10);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "label", 47);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](2, "Sygnatura KRS");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](3, "input", 48);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} }
function SearchFormComponent_ng_template_49_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](2, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4, "Przyk\u0142ad 1:");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "Data publikacji od: 2015-01-01");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](8, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](10, "Data publikacji do: 2020-01-01");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](11, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, "Przyk\u0142ad 2:");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](15, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](17, "Data publikacji od: 2012-01-01");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](18, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "Data publikacji do: 2017-01-01");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r9 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", ctx_r9.popoverTexts.dateFrom.text, " ");
} }
function SearchFormComponent_ng_template_57_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](1, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](2, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](4, "Przyk\u0142ad 1:");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](7, "Data publikacji od: 2016-01-01");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](8, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](10, "Data publikacji do: 2020-12-31");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](11, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](12, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](14, "Przyk\u0142ad 2:");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](15, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](16, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](17, "Data publikacji od: 2011-01-01");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](18, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "i");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "Data publikacji do: 2015-12-31");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r12 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", ctx_r12.popoverTexts.dateTo.text, " ");
} }
const _c0 = function (a1) { return ["/pobieranie-monitora", a1]; };
class SearchFormComponent {
    constructor(router, formBuilder, api, state) {
        this.router = router;
        this.formBuilder = formBuilder;
        this.api = api;
        this.state = state;
        this.popover = true;
        this.formOptionShow = false;
        this.alertWarning = false;
        this.fullsizeLoader = false;
        this.popoverTexts = {
            dateFrom: {
                text: "Zakres przeszukiwania.",
                title: '',
                example1: "Data publikacji od: 2017-01-01",
                example2: "Data publikacji do: 2023-01-01"
            },
            dateTo: {
                text: "Zakres przeszukiwania.",
                title: '',
                example1: "Data publikacji od: 2013-01-01",
                example2: "Data publikacji do: 2023-01-01"
            }
        };
        this.blockSearchButton = false;
        this.baseList = [
            {
                name: 'Baza ogłoszeń',
                val: 'A'
            },
            {
                name: 'Baza KRS',
                val: 'B'
            }
        ];
        this.hidesignatureKRS = false;
        this.year = new Date().getFullYear().toString();
        this.mindateControl = { year: 2001, month: 1, day: 1 };
    }
    searchList(popoverNip = '') {
        var _a, _b, _c;
        this.fullsizeLoader = true;
        let nipForm = this.searchForm.get('nip');
        let textInPosition = this.searchForm.get('textInPosition');
        let textInBody = this.searchForm.get('textInBody');
        let krsForm = this.searchForm.get('krs');
        let entityName = this.searchForm.get('entityName');
        if (entityName.value) {
            this.searchForm.value.entityName = entityName.value.replace(/[?&]/g, "%26");
        }
        if (krsForm.value) {
            this.fillZeros();
        }
        if (nipForm.value) {
            nipForm.setValue(nipForm.value.toString());
        }
        if (textInPosition.value) {
            this.searchForm.get('textInPosition').setValue(textInPosition.value.replace(/\n|\r/g, " "));
        }
        if (textInBody.value) {
            this.searchForm.get('textInBody').setValue(textInBody.value.replace(/\n|\r/g, " "));
        }
        let objToSent = {
            textInBody: (_a = textInBody.value) === null || _a === void 0 ? void 0 : _a.replace(/[?&]/g, "%26"),
            entityName: (_b = entityName.value) === null || _b === void 0 ? void 0 : _b.replace(/[?&]/g, "%26"),
            textInPosition: (_c = textInPosition.value) === null || _c === void 0 ? void 0 : _c.replace(/[?&]/g, "%26")
        };
        if (objToSent.entityName) {
            this.searchForm.value.entityName = objToSent.entityName;
        }
        if (objToSent.textInBody) {
            this.searchForm.value.textInBody = objToSent.textInBody;
        }
        if (objToSent.textInPosition) {
            this.searchForm.value.textInPosition = objToSent.textInPosition;
        }
        if (this.blockSearchButton === false) {
            this.serachSubscription = this.api.searchMonitor(this.searchForm.value).subscribe({
                next: res => {
                    this.fullsizeLoader = false;
                    let data = res;
                    if (data.list.length > 0) {
                        this.state.shareData(res);
                        this.state.shareSearchRequest(this.searchForm.value);
                        this.router.navigateByUrl('/list');
                    }
                    else {
                        this.state.shareAlertBody([{
                                status: 'info',
                                message: 'Brak wyników. Zmień kryteria wyszukiwania.',
                                alwaysVisible: false
                            }]);
                    }
                },
                error: err => {
                    this.fullsizeLoader = false;
                    this.state.shareAlertBody([{
                            status: 'danger',
                            message: 'Wystąpił bład.',
                            alwaysVisible: false
                        }]);
                }
            });
        }
        else {
            this.fullsizeLoader = false;
            // this.state.shareAlertBody([{
            //   status: 'danger',
            //   message: 'Wprowadzone nieprawidłowy numer NIP',
            //   alwaysVisible: false
            // }]);
            this.showNipWarning(popoverNip);
        }
    }
    ngOnInit() {
        this.selectTodayControl();
        this.searchForm = this.searchFormInit();
        this.nipValidation();
        var today = new Date();
        this.setDateRange('to', today, false, false, false, true);
        this.setDateRange('from', new Date(today.getFullYear() - 5, today.getMonth(), today.getDay(), 1, 1, 1, 1), false, false, false, true);
        this.searchForm.get('signatureOfCase').valueChanges.subscribe({
            next: res => {
                this.formOptionShow = (res === null || res === void 0 ? void 0 : res.length) > 0 ? true : false;
            }
        });
    }
    ngOnDestroy() {
        if (this.serachSubscription) {
            this.serachSubscription.unsubscribe();
        }
    }
    resetForm() {
        this.searchForm.get('entityName').setValue('');
        this.searchForm.get('krs').setValue('');
        this.searchForm.get('nip').setValue('');
        this.searchForm.get('textInPosition').setValue('');
        this.searchForm.get('textInBody').setValue('');
        this.searchForm.get('signatureOfCase').setValue('');
        this.searchForm.get('signatureKRS').setValue('');
        this.searchForm.get('court').setValue('');
        var today = new Date();
        this.setDateRange('to', today, false, false, false, true);
        this.setDateRange('from', new Date(today.getFullYear() - 5, today.getMonth(), today.getDay(), 1, 1, 1, 1), false, false, false, true);
    }
    selectTodayControl() {
        let d = new Date();
        let year = d.getFullYear();
        let month = d.getMonth() + 1;
        let day = d.getDate();
        this.todayDateControl = { year: year, month: month, day: day };
    }
    selectChange() {
        let select = this.searchForm.get('signatureType').value;
        if (select == "B") {
            this.hidesignatureKRS = true;
            this.searchForm.get('signatureOfCase').setValue('');
        }
        else {
            this.hidesignatureKRS = false;
            this.searchForm.get('signatureKRS').setValue('');
        }
    }
    formatDatePicker(date) {
        // null is case for today
        let d = date ? new Date(date) : new Date();
        let year = d.getFullYear();
        let month = d.getMonth() + 1;
        let day = d.getDate();
        return { year: year, month: month, day: day };
    }
    setDateRange(formControl, date, getFive = true, setToday = false, setMin = false, init = false) {
        if (init) {
            if (formControl == "from") {
                this.startDateFrom = null;
                let formDateFrom;
                this.startDateFrom = { year: date.getFullYear(), month: date.getMonth() + 1, day: date.getDate() };
                formDateFrom = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
                this.searchForm.get('from').setValue(formDateFrom);
            }
            if (formControl == "to") {
                this.startDateTo = null;
                let formDateTo;
                // format for datapicker
                this.startDateTo = { year: date.getFullYear(), month: date.getMonth() + 1, day: date.getDate() };
                this.minFrom = this.startDateFrom;
                // format for api
                formDateTo = `${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate()}`;
                this.searchForm.get('to').setValue(formDateTo);
            }
        }
        else {
            let minDate = new Date('2001-01-01');
            let maxDate = new Date();
            let dateFrom = new Date(this.searchForm.get('from').value);
            let dateTo = new Date(this.searchForm.get('to').value);
            if (dateFrom > maxDate) {
                dateFrom = maxDate;
            }
            if (dateTo > maxDate) {
                dateTo = maxDate;
            }
            if (dateFrom < minDate) {
                dateFrom = minDate;
            }
            if (dateTo < minDate) {
                dateTo = minDate;
            }
            if (formControl == "from" && dateFrom > dateTo) {
                dateTo = new Date(this.searchForm.get('from').value);
            }
            if (formControl == "to" && dateFrom > dateTo) {
                dateFrom = new Date(this.searchForm.get('to').value);
            }
            this.startDateFrom = null;
            this.startDateTo = null;
            let formDateFrom;
            let formDateTo;
            // format for datapicker
            this.startDateFrom = { year: dateFrom.getFullYear(), month: dateFrom.getMonth() + 1, day: dateFrom.getDate() };
            this.startDateTo = { year: dateTo.getFullYear(), month: dateTo.getMonth() + 1, day: dateTo.getDate() };
            this.minFrom = this.startDateFrom;
            // format for api
            formDateFrom = `${dateFrom.getFullYear()}-${dateFrom.getMonth() + 1}-${dateFrom.getDate()}`;
            formDateTo = `${dateTo.getFullYear()}-${dateTo.getMonth() + 1}-${dateTo.getDate()}`;
            this.searchForm.get('from').setValue(formDateFrom);
            this.searchForm.get('to').setValue(formDateTo);
        }
    }
    createDatesObj(date) {
        let year = date.getFullYear();
        let month = date.getMonth() + 1;
        let monthDD = ((date.getMonth() + 1) < 10 ? '0' : '') + (date.getMonth() + 1);
        let day = date.getDate();
        let dayDD = (date.getDate() < 10 ? '0' : '') + date.getDate();
        return {
            dateApi: { year: year, month: monthDD, day: dayDD },
            datePicker: { year: year, month: month, day: day }
        };
    }
    searchFormInit() {
        return this.formBuilder.group({
            entityName: [''],
            krs: [''],
            nip: ['', [_CheckNipValidator__WEBPACK_IMPORTED_MODULE_2__["CheckNipValidator"].checkNip]],
            textInPosition: ['', [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].maxLength(1000)]],
            textInBody: ['', [_angular_forms__WEBPACK_IMPORTED_MODULE_1__["Validators"].maxLength(1000)]],
            signatureType: [this.baseList[0].val],
            signatureOfCase: [''],
            signatureKRS: [''],
            court: [''],
            from: [''],
            to: [''],
            page: [1],
        });
    }
    nipValidation() {
        this.searchForm.get('nip').valueChanges.subscribe({
            next: value => {
                var _a;
                let val = value == undefined ? '' : value.toString();
                let input = this.searchForm.get('nip');
                if (val.length > 0 && !((_a = input.errors) === null || _a === void 0 ? void 0 : _a.checkNip)) {
                    this.blockSearchButton = true;
                }
                else {
                    this.blockSearchButton = false;
                    if (this.instanceOfPopover) {
                        this.instanceOfPopover.close();
                        this.instanceOfPopover = '';
                    }
                }
            }
        });
    }
    showNipWarning(popover) {
        var _a, _b;
        let input = this.searchForm.get('nip');
        let val = (_a = input.value) === null || _a === void 0 ? void 0 : _a.toString();
        val = val == undefined ? '' : val;
        if (val.length > 0 && !((_b = input.errors) === null || _b === void 0 ? void 0 : _b.checkNip)) {
            this.instanceOfPopover = popover;
            popover.open();
            this.blockSearchButton = true;
        }
        else {
            this.blockSearchButton = false;
            this.instanceOfPopover = '';
        }
    }
    fillZeros() {
        let krsForm = this.searchForm.get('krs');
        let valueWithZeros;
        let zeros;
        if (krsForm.value.length > 0 && krsForm.value.length < 10) {
            let howManyLoops = 10 - krsForm.value.length;
            for (let i = 0; i < howManyLoops; i++) {
                zeros = zeros ? zeros : '';
                zeros = `${zeros}0`;
            }
            valueWithZeros = `${zeros}${krsForm.value}`;
            krsForm.setValue(valueWithZeros);
        }
    }
    dateSelected(formControl, value) {
        let dateFrom = new Date(value);
        this.searchForm.get(formControl).setValue(dateFrom);
        this.setDateRange(formControl, dateFrom);
    }
    compareByID(itemOne, itemTwo) {
        return itemOne && itemTwo && itemOne.ID == itemTwo.ID;
    }
}
SearchFormComponent.ɵfac = function SearchFormComponent_Factory(t) { return new (t || SearchFormComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormBuilder"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_api_service__WEBPACK_IMPORTED_MODULE_4__["ApiService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_services_state_service__WEBPACK_IMPORTED_MODULE_5__["StateService"])); };
SearchFormComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: SearchFormComponent, selectors: [["search-form"]], decls: 69, vars: 25, consts: [[4, "ngIf"], [1, "subTitle", "px-3"], [1, "fluid-container", "d-flex", "flex-wrap", "justify-content-center"], ["aria-label", "Wyszukiwanie og\u0142osze\u0144", 1, "title"], [1, "container", 2, "margin-top", "25px", 3, "formGroup"], [1, "row"], [1, "mb-5"], [1, "row", 2, "text-align", "center", "display", "block"], ["role", "link", "aria-label", "Przejd\u017A do pobierz monitor", "alt", "Pobierz monitor", 1, "btn", "btn-link", "table-action_link", "mt-2", 2, "font-size", "1.1rem", "font-weight", "500", 3, "routerLink"], [1, "col-sm-12", "col-md-6"], [1, "mb-2"], ["for", "formControlEntityName", 1, "form-label"], ["aria-label", "Wpisz nazw\u0119 podmiotu", "formControlName", "entityName", "autocomplete", "off", "type", "text", "id", "formControlEntityName", "placeholder", "Wpisz nazw\u0119 podmiotu", 1, "form-control", 3, "keyup.enter"], ["for", "formControlKrs", 1, "form-label"], ["formControlName", "krs", "autocomplete", "off", "mask", "0000000000", "aria-label", "Wpisz KRS", "type", "text", "id", "formControlKrs", "placeholder", "Podaj nr KRS", 1, "form-control", 3, "keyup.enter", "blur"], ["popoverNip", ""], ["for", "formControlNip", 1, "form-label"], ["onkeydown", "return event.keyCode !== 69", "formControlName", "nip", "autocomplete", "off", "type", "text", "aria-label", "Wpisz NIP", "maxlength", "13", "id", "formControlNip", "placeholder", "Podaj NIP", "triggers", "manual", 1, "form-control", 3, "ngbPopover", "autoClose", "blur", "keyup.enter"], ["p2", "ngbPopover"], ["for", "textInPosition", 1, "form-label"], ["formControlName", "textInPosition", "autocomplete", "off", "maxlength", "1000", "aria-label", "Wpisz lub wklej tekst w tre\u015Bci", "id", "textInPosition", "rows", "4", "placeholder", "Wpisz szukany tekst", 1, "form-control", 3, "keyup.enter"], ["for", "textInBody", 1, "form-label"], ["formControlName", "textInBody", "maxlength", "1000", "autocomplete", "off", "aria-label", "Wpisz lub wklej tekst w tre\u015Bci", "id", "textInBody", "rows", "4", "placeholder", "Wpisz szukany tekst", 1, "form-control", 3, "keyup.enter"], ["for", "signatureType", 1, "form-label"], ["formControlName", "signatureType", "aria-label", "wybierz Typ og\u0142oszenia lub sprawy", "aria-label", "Default select example", 1, "form-control", 3, "compareWith", "change"], [3, "aria-label", "ngValue", 4, "ngFor", "ngForOf"], ["class", "mb-2", 4, "ngIf"], ["for", "formControlDateFrom", 1, "form-label"], ["popContent", ""], ["tabindex", "0", 1, "bi", "bi-info-circle", "information-title", 3, "ngbPopover", "autoClose", "keyup.enter"], ["p3", "ngbPopover"], ["aria-label", "Wybierz dat\u0119 publikacji do. Prze\u0142\u0105czaj si\u0119 strza\u0142kami i klawiszem TAB, akceptacja nacisnij Enter, cofni\u0119cie si\u0119 z danej sekcji daty to ESC", 3, "minDate", "maxDate", "startValue", "popover", "valueSelected"], ["for", "formControlDateTo", 1, "form-label"], ["p4", "ngbPopover"], [1, "col"], [1, "mb-2", "d-flex", "flex-wrap", "justify-content-end"], ["type", "button", "aria-label", "Przycisk formularza szukaj", "alt", "Szukaj", 1, "btn", "btn-primary", "mr-3", 3, "disabled", "click"], ["type", "button", "role", "button", "alt", "wyczy\u015B\u0107 formularz", "aria-label", "Wyczy\u015B\u0107 formularz", 1, "btn", "btn-secondary", 3, "click"], [1, "error"], [3, "aria-label", "ngValue"], ["for", "signatureOfCase", 1, "form-label"], ["tabindex", "0", "ngbPopover", "Prosimy wpisa\u0107 numer sprawy nadanej przez s\u0105d", 1, "bi", "bi-info-circle", "information-title", 3, "autoClose", "keyup.enter"], ["p1", "ngbPopover"], ["formControlName", "signatureOfCase", "aria-label", "Wpisz sygnatur\u0119 sprawy", "autocomplete", "off", "type", "text", "id", "signatureOfCase", "placeholder", "Sygnatura sprawy", 1, "form-control"], ["for", "court", 1, "form-label"], ["tabindex", "0", "ngbPopover", "Prosz\u0119 wskaza\u0107 s\u0105d, w kt\u00F3rym toczy si\u0119 post\u0119powanie", 1, "bi", "bi-info-circle", "information-title", 3, "autoClose", "keyup.enter"], ["formControlName", "court", "autocomplete", "off", "aria-label", "Prosz\u0119 wskaza\u0107 s\u0105d, w kt\u00F3rym toczy si\u0119 post\u0119powanie", "type", "text", "id", "court", "placeholder", "Miasto", 1, "form-control"], ["for", "signatureKRS", 1, "form-label"], ["formControlName", "signatureKRS", "autocomplete", "off", "type", "text", "aria-label", "Wpisz Sygnatur\u0119 KRS", "id", "signatureKRS", "placeholder", "Wpisz sygnatur\u0119 KRS", 1, "form-control"]], template: function SearchFormComponent_Template(rf, ctx) { if (rf & 1) {
        const _r22 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](0, SearchFormComponent_fullsize_loader_0_Template, 1, 0, "fullsize-loader", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "main-header");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "div", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](5, "Wyszukiwanie og\u0142osze\u0144");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](6, "div", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](7, "div", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](8, "div", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](9, "div", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](10, "a", 8);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](11, "Pobierz monitor");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](12, "div", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](13, "div", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](14, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](15, "label", 11);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](16, "Nazwa podmiotu");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](17, "input", 12);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_Template_input_keyup_enter_17_listener() { return ctx.searchList(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](18, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](19, "label", 13);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](20, "Numer KRS");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](21, "input", 14);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_Template_input_keyup_enter_21_listener() { return ctx.searchList(); })("blur", function SearchFormComponent_Template_input_blur_21_listener() { return ctx.fillZeros(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](22, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](23, SearchFormComponent_ng_template_23_Template, 2, 0, "ng-template", null, 15, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplateRefExtractor"]);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](25, "label", 16);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](26, "NIP");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](27, "input", 17, 18);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("blur", function SearchFormComponent_Template_input_blur_27_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r22); const _r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](28); return ctx.showNipWarning(_r3); })("keyup.enter", function SearchFormComponent_Template_input_keyup_enter_27_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r22); const _r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](28); return ctx.searchList(_r3); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](29, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](30, "label", 19);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](31, "Tekst w pozycji");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](32, "textarea", 20);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_Template_textarea_keyup_enter_32_listener() { return ctx.searchList(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](33, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](34, "label", 21);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](35, "Tekst w tre\u015Bci");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](36, "textarea", 22);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_Template_textarea_keyup_enter_36_listener() { return ctx.searchList(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](37, "div", 9);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](38, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](39, "label", 23);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](40, "Typ og\u0142./sprawy");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](41, "select", 24);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("change", function SearchFormComponent_Template_select_change_41_listener() { return ctx.selectChange(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](42, SearchFormComponent_option_42_Template, 2, 3, "option", 25);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](43, SearchFormComponent_div_43_Template, 6, 1, "div", 26);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](44, SearchFormComponent_div_44_Template, 6, 1, "div", 26);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](45, SearchFormComponent_div_45_Template, 4, 0, "div", 26);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](46, "div", 10);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](47, "label", 27);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](48, "Data publikacji od ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](49, SearchFormComponent_ng_template_49_Template, 21, 1, "ng-template", null, 28, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplateRefExtractor"]);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](51, "span", 29, 30);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_Template_span_keyup_enter_51_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r22); const _r10 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](52); return _r10.open(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](53, "app-date-picker", 31);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("valueSelected", function SearchFormComponent_Template_app_date_picker_valueSelected_53_listener($event) { return ctx.dateSelected("from", $event); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](54, "div", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](55, "label", 32);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](56, "Data publikacji do ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](57, SearchFormComponent_ng_template_57_Template, 21, 1, "ng-template", null, 28, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplateRefExtractor"]);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](59, "span", 29, 33);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("keyup.enter", function SearchFormComponent_Template_span_keyup_enter_59_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r22); const _r13 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](60); return _r13.open(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](61, "app-date-picker", 31);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("valueSelected", function SearchFormComponent_Template_app_date_picker_valueSelected_61_listener($event) { return ctx.dateSelected("to", $event); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](62, "div", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](63, "div", 34);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](64, "div", 35);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](65, "button", 36);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function SearchFormComponent_Template_button_click_65_listener() { return ctx.searchList(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](66, " Szukaj ");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](67, "button", 37);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function SearchFormComponent_Template_button_click_67_listener() { return ctx.resetForm(); });
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](68, "Wyczy\u015B\u0107");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } if (rf & 2) {
        const _r1 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](24);
        const _r8 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵreference"](50);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.fullsizeLoader);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("formGroup", ctx.searchForm);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpureFunction1"](23, _c0, ctx.year));
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](17);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngbPopover", _r1)("autoClose", false);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](14);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("compareWith", ctx.compareByID);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx.baseList);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", !ctx.hidesignatureKRS);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.formOptionShow);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.hidesignatureKRS);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngbPopover", _r8)("autoClose", true);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("minDate", ctx.mindateControl)("maxDate", ctx.todayDateControl)("startValue", ctx.startDateFrom)("popover", ctx.popoverTexts.dateFrom);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](6);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngbPopover", _r8)("autoClose", true);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](2);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("minDate", ctx.mindateControl)("maxDate", ctx.todayDateControl)("startValue", ctx.startDateTo)("popover", ctx.popoverTexts.dateTo);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](4);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("disabled", ctx.blockSearchButton);
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_6__["NgIf"], _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_7__["MainHeaderComponent"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgControlStatusGroup"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormGroupDirective"], _angular_router__WEBPACK_IMPORTED_MODULE_3__["RouterLinkWithHref"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["DefaultValueAccessor"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgControlStatus"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormControlName"], ngx_mask__WEBPACK_IMPORTED_MODULE_8__["MaskDirective"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["MaxLengthValidator"], _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_9__["NgbPopover"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["SelectControlValueAccessor"], _angular_common__WEBPACK_IMPORTED_MODULE_6__["NgForOf"], _date_picker_date_picker_component__WEBPACK_IMPORTED_MODULE_10__["DatePickerComponent"], _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_11__["FullsizeLoaderComponent"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["NgSelectOption"], _angular_forms__WEBPACK_IMPORTED_MODULE_1__["ɵangular_packages_forms_forms_x"]], styles: ["input[_ngcontent-%COMP%]::-webkit-outer-spin-button, input[_ngcontent-%COMP%]::-webkit-inner-spin-button {\n  -webkit-appearance: none;\n  margin: 0;\n}\n\ninput[type=number][_ngcontent-%COMP%] {\n  -moz-appearance: textfield;\n}\n.error[_ngcontent-%COMP%] {\n  color: #d5233f;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9zdHlsZXMvY29sb3JzLnNjc3MiLCJzcmMvYXBwL3NlYXJjaC1mb3JtL3NlYXJjaC1mb3JtLmNvbXBvbmVudC5zY3NzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLGdCQUFBO0FDRUEsZ0NBQUE7QUFDQTs7RUFFRSx3QkFBQTtFQUNBLFNBQUE7QUFBRjtBQUdBLFlBQUE7QUFDQTtFQUNFLDBCQUFBO0FBQUY7QUFHQTtFQUNFLGNET1k7QUNQZCIsImZpbGUiOiJzcmMvYXBwL3NlYXJjaC1mb3JtL3NlYXJjaC1mb3JtLmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiLyogYmFzZSBjb2xvcnMgKi9cclxuXHJcbiRjb2xvcl9ncmV5XzE6ICMwZDBkMGQ7IFxyXG4kY29sb3JfZ3JleV8yOiAjMzMzMzMzOyBcclxuJGNvbG9yX2dyZXlfMzogIzRkNGQ0ZDsgXHJcbiRjb2xvcl9ncmV5XzQ6ICM2NjY7XHJcbiRjb2xvcl9ncmV5XzU6ICNiMmIyYjI7XHJcbiRjb2xvcl9ncmV5XzY6ICNkOWQ5ZDk7XHJcbiRjb2xvcl9ncmV5XzY6ICNmNWY1ZjU7ICBcclxuXHJcbiRjb2xvcl9ibHVlXzE6ICMwMDMzNjY7IFxyXG4kY29sb3JfYmx1ZV8yOiAjMDA0Mjg0OyBcclxuJGNvbG9yX2JsdWVfMzogIzAwNTJhNTsgXHJcbiRjb2xvcl9ibHVlXzQ6ICM5OWNjZmY7IFxyXG4kY29sb3JfYmx1ZV81OiAjZjVmYWZmOyBcclxuXHJcbiRjb2xvcl9ncmVlbl8xOiAjMTgzNTE4OyBcclxuJGNvbG9yX2dyZWVuXzI6ICMzYTgyM2E7IFxyXG4kY29sb3JfZ3JlZW5fMzogI2I5ZGZiOTsgXHJcbiRjb2xvcl9ncmVlbl80OiAjZWRmN2VkOyBcclxuXHJcbiRjb2xvcl9yZWRfMTogIzY2MDAwYTsgXHJcbiRjb2xvcl9yZWRfMjogI2Q1MjMzZjsvLyNhODAwMTE7IFxyXG4kY29sb3JfcmVkXzM6ICNmZmIyYmE7IFxyXG4kY29sb3JfcmVkXzQ6ICNmZmYwZjE7XHJcblxyXG4kY29sb3JfaW5mXzE6ICMwNDQzNjI7IFxyXG4kY29sb3JfaW5mXzI6ICMwNjVhODQ7IFxyXG4kY29sb3JfaW5mXzM6ICNiNWU1ZmM7IFxyXG4kY29sb3JfaW5mXzQ6ICNmNWZiZmY7XHJcblxyXG4kY29sb3Jfd2FybmluZ18xOiAjNTc0MTAwOyBcclxuJGNvbG9yX3dhcm5pbmdfMjogI2U1YWMwMDsgXHJcbiRjb2xvcl93YXJuaW5nXzM6ICNmZmRmODA7IFxyXG4kY29sb3Jfd2FybmluZ180OiAjZmZmOWU1O1xyXG5cclxuJGNvbnRyYXN0X2JhY2tncm91bnVkOiAjMGQwZDBkO1xyXG4kY29udHJhc3RfZm9udDogI2ZmZjcwMDtcclxuJGNvbnRyYXN0X2xpbms6ICNmZmY7XHJcblxyXG4iLCJAaW1wb3J0IFwiLi4vLi4vc3R5bGVzL2NvbG9ycy5zY3NzXCI7IFxyXG5cclxuLyogQ2hyb21lLCBTYWZhcmksIEVkZ2UsIE9wZXJhICovXHJcbmlucHV0Ojotd2Via2l0LW91dGVyLXNwaW4tYnV0dG9uLFxyXG5pbnB1dDo6LXdlYmtpdC1pbm5lci1zcGluLWJ1dHRvbiB7XHJcbiAgLXdlYmtpdC1hcHBlYXJhbmNlOiBub25lO1xyXG4gIG1hcmdpbjogMDtcclxufVxyXG5cclxuLyogRmlyZWZveCAqL1xyXG5pbnB1dFt0eXBlPW51bWJlcl0ge1xyXG4gIC1tb3otYXBwZWFyYW5jZTogdGV4dGZpZWxkO1xyXG59XHJcblxyXG4uZXJyb3J7XHJcbiAgY29sb3I6ICRjb2xvcl9yZWRfMjtcclxuICAvLyBib3JkZXI6IDFweCBzb2xpZCByZWQ7XHJcbn0iXX0= */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](SearchFormComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'search-form',
                templateUrl: './search-form.component.html',
                styleUrls: ['./search-form.component.scss']
            }]
    }], function () { return [{ type: _angular_router__WEBPACK_IMPORTED_MODULE_3__["Router"] }, { type: _angular_forms__WEBPACK_IMPORTED_MODULE_1__["FormBuilder"] }, { type: _services_api_service__WEBPACK_IMPORTED_MODULE_4__["ApiService"] }, { type: _services_state_service__WEBPACK_IMPORTED_MODULE_5__["StateService"] }]; }, null); })();


/***/ }),

/***/ "./src/app/services/Interceptor.ts":
/*!*****************************************!*\
  !*** ./src/app/services/Interceptor.ts ***!
  \*****************************************/
/*! exports provided: MyInterceptor */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MyInterceptor", function() { return MyInterceptor; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");
/* harmony import */ var rxjs_operators__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! rxjs/operators */ "./node_modules/rxjs/_esm2015/operators/index.js");





class MyInterceptor {
    intercept(req, next) {
        return next.handle(req).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_2__["map"])(event => {
            return event;
        }), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_2__["catchError"])(error => {
            MyInterceptor.ShowError.next(error);
            // console.error('stop', error);
            return Object(rxjs__WEBPACK_IMPORTED_MODULE_1__["throwError"])(error);
        }), Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_2__["finalize"])(() => {
        }));
    }
}
MyInterceptor.ShowError = new rxjs__WEBPACK_IMPORTED_MODULE_1__["Subject"]();
MyInterceptor.ɵfac = function MyInterceptor_Factory(t) { return new (t || MyInterceptor)(); };
MyInterceptor.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: MyInterceptor, factory: MyInterceptor.ɵfac });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](MyInterceptor, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"]
    }], null, null); })();


/***/ }),

/***/ "./src/app/services/api.service.ts":
/*!*****************************************!*\
  !*** ./src/app/services/api.service.ts ***!
  \*****************************************/
/*! exports provided: ApiService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ApiService", function() { return ApiService; });
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common/http */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/http.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _state_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./state.service */ "./src/app/services/state.service.ts");






//export const API_URL = 'https://localhost:5001/api';//'http://192.168.30.57:777/api'
class ApiService {
    constructor(document, http, state) {
        this.document = document;
        this.http = http;
        this.state = state;
        this.httpOptions = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({
                "Content-Type": "application/json",
                "Accept": "text/plain"
            }),
            withCredentials: true
        };
        this.httpOptionsUrl = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({
                "Content-Type": "text/plain",
                "Accept": "text/plain"
            }),
            withCredentials: true
        };
        this.httpFileUpload = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({
                "Accept": "application/json"
            }),
            withCredentials: true
        };
        this.httpFileDownload = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({
                "Accept": "blob",
                "Access-Control-Expose-Headers": "*",
                "Content-Type": "application/ms-excel",
            }),
            responseType: 'blob',
            withCredentials: true,
        };
        this.httpFileDownload2 = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({
                'Accept': 'application/pdf',
                'Access-Control-Expose-Headers': 'Content-Disposition',
                "Content-Type": "application/octet-stream",
            }),
            observe: 'response',
            responseType: 'blob',
            withCredentials: true,
        };
        this.httpFileDownload3 = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({
                "Accept": "blob",
                'Access-Control-Expose-Headers': '*',
                "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            }),
            observe: 'response',
            responseType: 'blob',
            withCredentials: true,
        };
        this.state.url$.subscribe({
            next: url => {
                this.apiURL = url;
            }
        });
    }
    getApiUrl() {
        let url = `${document.location.origin}/`; //document.location.href;
        this.http.get(`${url}home/getapiurl`, { responseType: 'text' }).subscribe({
            next: res => {
                this.apiURL = res;
                this.state.shareUrl(this.apiURL);
            },
            error: err => {
                console.log(err);
            }
        });
    }
    makeUrlForGetMethod(data) {
        let urlForGetMethod;
        let i = 0;
        for (let key in data) {
            if (data.hasOwnProperty(key)) {
                i++;
                urlForGetMethod = `${i === 1 ? '?' : ''}${urlForGetMethod ? urlForGetMethod : ''}${i === 1 ? '' : '&'}${key}=${data[key]}`;
                let value = data[key];
            }
        }
        return urlForGetMethod;
    }
    searchMonitor(data) {
        let values = this.makeUrlForGetMethod(data);
        return this.http.get(`${this.apiURL}/Monitor/Search${values}`, this.httpOptions);
    }
    searchMonitorCount(data) {
        let values = this.makeUrlForGetMethod(data);
        return this.http.get(`${this.apiURL}/Monitor/SearchCount${values}`, this.httpOptions);
    }
    getMonitorDetails(id) {
        return this.http.get(`${this.apiURL}/Monitor/Detalis?Id=${id}`, this.httpOptions);
    }
    getFileMonitor(id) {
        return this.http.get(`${this.apiURL}/Monitor/Download?id=${id}`, this.httpOptions);
    }
    getMonitorByYear(year) {
        return this.http.get(`${this.apiURL}/Monitor/GetFiles?year=${year}`, this.httpOptions);
    }
}
ApiService.ɵfac = function ApiService_Factory(t) { return new (t || ApiService)(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵinject"](_angular_common__WEBPACK_IMPORTED_MODULE_2__["DOCUMENT"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵinject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpClient"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵinject"](_state_service__WEBPACK_IMPORTED_MODULE_3__["StateService"])); };
ApiService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjectable"]({ token: ApiService, factory: ApiService.ɵfac, providedIn: 'root' });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](ApiService, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Injectable"],
        args: [{
                providedIn: 'root'
            }]
    }], function () { return [{ type: undefined, decorators: [{
                type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Inject"],
                args: [_angular_common__WEBPACK_IMPORTED_MODULE_2__["DOCUMENT"]]
            }] }, { type: _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpClient"] }, { type: _state_service__WEBPACK_IMPORTED_MODULE_3__["StateService"] }]; }, null); })();


/***/ }),

/***/ "./src/app/services/format-bytes.pipe.ts":
/*!***********************************************!*\
  !*** ./src/app/services/format-bytes.pipe.ts ***!
  \***********************************************/
/*! exports provided: FormatBytesPipe */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FormatBytesPipe", function() { return FormatBytesPipe; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");


class FormatBytesPipe {
    transform(value, decimals = 2) {
        if (value === 0)
            return '0 KB';
        const k = 1024;
        const dm = decimals < 0 ? 0 : decimals;
        const sizes = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
        const i = Math.floor(Math.log(value) / Math.log(k));
        return parseFloat((value / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
    }
}
FormatBytesPipe.ɵfac = function FormatBytesPipe_Factory(t) { return new (t || FormatBytesPipe)(); };
FormatBytesPipe.ɵpipe = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefinePipe"]({ name: "formatBytes", type: FormatBytesPipe, pure: true });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](FormatBytesPipe, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Pipe"],
        args: [{
                name: 'formatBytes'
            }]
    }], null, null); })();


/***/ }),

/***/ "./src/app/services/state.service.ts":
/*!*******************************************!*\
  !*** ./src/app/services/state.service.ts ***!
  \*******************************************/
/*! exports provided: StateService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "StateService", function() { return StateService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var rxjs__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! rxjs */ "./node_modules/rxjs/_esm2015/index.js");



class StateService {
    constructor() {
        this.data$ = new rxjs__WEBPACK_IMPORTED_MODULE_1__["BehaviorSubject"](null);
        this.searchRequest$ = new rxjs__WEBPACK_IMPORTED_MODULE_1__["BehaviorSubject"](null);
        this.alertBody$ = new rxjs__WEBPACK_IMPORTED_MODULE_1__["Subject"]();
        this.url$ = new rxjs__WEBPACK_IMPORTED_MODULE_1__["BehaviorSubject"](null);
        this.accessibility$ = new rxjs__WEBPACK_IMPORTED_MODULE_1__["BehaviorSubject"](null);
    }
    shareData(data = null) {
        this.data$.next(data);
    }
    shareSearchRequest(data = null) {
        this.searchRequest$.next(data);
    }
    shareAlertBody(body) {
        this.alertBody$.next(body);
    }
    shareUrl(url) {
        this.url$.next(url);
    }
    shareAccessibility(data) {
        this.accessibility$.next(data);
    }
}
StateService.ɵfac = function StateService_Factory(t) { return new (t || StateService)(); };
StateService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: StateService, factory: StateService.ɵfac, providedIn: 'root' });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](StateService, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
        args: [{
                providedIn: 'root'
            }]
    }], null, null); })();


/***/ }),

/***/ "./src/app/shared/alert/alert.component.ts":
/*!*************************************************!*\
  !*** ./src/app/shared/alert/alert.component.ts ***!
  \*************************************************/
/*! exports provided: AlertComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AlertComponent", function() { return AlertComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");



const _c0 = ["alert"];
function AlertComponent_div_0_ng_container_3_ng_container_1_div_2_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 12);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtext"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const item_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"](2).$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtextInterpolate1"](" ", item_r3.message, " ");
} }
function AlertComponent_div_0_ng_container_3_ng_container_1_Template(rf, ctx) { if (rf & 1) {
    const _r10 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](2, AlertComponent_div_0_ng_container_3_ng_container_1_div_2_Template, 2, 1, "div", 6);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](3, "div", 7);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](4, "div", 8);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵlistener"]("click", function AlertComponent_div_0_ng_container_3_ng_container_1_Template_div_click_4_listener($event) { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵrestoreView"](_r10); const i_r4 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().index; const ctx_r8 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"](2); return ctx_r8.closeAlert(i_r4, $event); });
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](5, "svg", 9);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](6, "path", 10);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](7, "path", 11);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const item_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]().$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵclassMapInterpolate1"]("alert-body animated faster fadeIn ", item_r3.status, "");
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", item_r3.message);
} }
function AlertComponent_div_0_ng_container_3_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerStart"](0);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](1, AlertComponent_div_0_ng_container_3_ng_container_1_Template, 8, 4, "ng-container", 5);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainerEnd"]();
} if (rf & 2) {
    const item_r3 = ctx.$implicit;
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", item_r3 != null);
} }
function AlertComponent_div_0_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 1, 2);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](2, "div", 3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](3, AlertComponent_div_0_ng_container_3_Template, 2, 1, "ng-container", 4);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r0 = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngForOf", ctx_r0.alertConf);
} }
class AlertComponent {
    constructor(el, renderer) {
        this.el = el;
        this.renderer = renderer;
        this.closedAlert = new _angular_core__WEBPACK_IMPORTED_MODULE_0__["EventEmitter"]();
        this.duration = 5000;
    }
    ngOnInit() {
        if (!Array.isArray(this.alertConf))
            this.alertConf = [this.alertConf];
    }
    ngAfterViewInit() {
        var _a;
        this.alertDiv = (_a = this.alert) === null || _a === void 0 ? void 0 : _a.nativeElement;
        this.alertConf.forEach(item => {
            if (item.alwaysVisible)
                return;
            setTimeout(() => {
                this.closeAlert();
            }, this.duration);
        });
    }
    closeAlert(index = null, e = null) {
        if (e) {
            let alertEl = e.target.parentElement.parentElement.parentElement.parentElement;
            this.renderer.removeClass(alertEl, 'fadeIn');
            this.renderer.addClass(alertEl, 'fadeOut');
            setTimeout(() => {
                this.alertConf.splice(index, 1);
                if (this.alertConf.length == 0)
                    this.closedAlert.emit(true);
            }, 400);
        }
        else {
            this.renderer.addClass(this.alertDiv, 'animated');
            this.renderer.addClass(this.alertDiv, 'fadeOut');
            setTimeout(() => {
                this.closedAlert.emit(true);
            }, 300);
        }
    }
}
AlertComponent.ɵfac = function AlertComponent_Factory(t) { return new (t || AlertComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ElementRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["Renderer2"])); };
AlertComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: AlertComponent, selectors: [["alert"]], viewQuery: function AlertComponent_Query(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵviewQuery"](_c0, true);
    } if (rf & 2) {
        var _t;
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵloadQuery"]()) && (ctx.alert = _t.first);
    } }, inputs: { alertConf: "alertConf" }, outputs: { closeAlertTime: "closeAlertTime", closedAlert: "closedAlert" }, decls: 1, vars: 1, consts: [["class", "alert-wraper", 4, "ngIf"], [1, "alert-wraper"], ["alert", ""], [1, "container", 2, "padding-left", "0px !important", "padding-right", "0px !important"], [4, "ngFor", "ngForOf"], [4, "ngIf"], ["class", "message", 4, "ngIf"], [1, "close-alert"], [3, "click"], ["xmlns", "http://www.w3.org/2000/svg", "width", "16", "height", "16", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-x-lg"], ["fill-rule", "evenodd", "d", "M13.854 2.146a.5.5 0 0 1 0 .708l-11 11a.5.5 0 0 1-.708-.708l11-11a.5.5 0 0 1 .708 0Z"], ["fill-rule", "evenodd", "d", "M2.146 2.146a.5.5 0 0 0 0 .708l11 11a.5.5 0 0 0 .708-.708l-11-11a.5.5 0 0 0-.708 0Z"], [1, "message"]], template: function AlertComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵtemplate"](0, AlertComponent_div_0_Template, 4, 1, "div", 0);
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵproperty"]("ngIf", ctx.alertConf);
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_1__["NgIf"], _angular_common__WEBPACK_IMPORTED_MODULE_1__["NgForOf"]], styles: [".alert-wraper[_ngcontent-%COMP%] {\n  position: absolute;\n  margin-top: 150px;\n  width: 100%;\n  z-index: 100;\n  transition: all 0.3s ease-in-out !important;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body[_ngcontent-%COMP%] {\n  position: relative;\n  top: 0px;\n  width: 100%;\n  color: #0d0d0d;\n  z-index: 1;\n  display: flex;\n  flex-flow: column;\n  justify-content: center;\n  align-items: center;\n  height: 52px;\n  margin-bottom: 2px;\n  box-shadow: unset;\n  letter-spacing: 0.5px;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body[_ngcontent-%COMP%]:last-of-type {\n  z-index: 2;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body[_ngcontent-%COMP%]   .message[_ngcontent-%COMP%] {\n  width: 100%;\n  padding: 15px;\n  text-align: left;\n  color: #0d0d0d;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body.info[_ngcontent-%COMP%] {\n  background-color: #fff;\n  border: 2px solid #065a84;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body.success[_ngcontent-%COMP%] {\n  background-color: #fff;\n  border: 2px solid #3a823a;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body.danger[_ngcontent-%COMP%] {\n  background-color: #fff;\n  border: 2px solid #d5233f;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body.warning[_ngcontent-%COMP%] {\n  background-color: #fff;\n  border: 2px solid #e5ac00;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body[_ngcontent-%COMP%]   .close-alert[_ngcontent-%COMP%] {\n  position: absolute;\n  right: 0px;\n  width: 50px;\n  box-shadow: unset;\n  cursor: pointer;\n}\n.alert-wraper[_ngcontent-%COMP%]   .alert-body[_ngcontent-%COMP%]   .close-alert[_ngcontent-%COMP%]   div[_ngcontent-%COMP%] {\n  text-align: right;\n  padding-right: 15px;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9zdHlsZXMvY29sb3JzLnNjc3MiLCJzcmMvYXBwL3NoYXJlZC9hbGVydC9hbGVydC5jb21wb25lbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQSxnQkFBQTtBQ0dBO0VBRUksa0JBQUE7RUFDQSxpQkFBQTtFQUNBLFdBQUE7RUFDQSxZQUFBO0VBQ0EsMkNBQUE7QUFGSjtBQUlJO0VBQ0ksa0JBQUE7RUFDQSxRQUFBO0VBQ0EsV0FBQTtFQUNBLGNEYk87RUNnQlAsVUFBQTtFQUNBLGFBQUE7RUFDQSxpQkFBQTtFQUNBLHVCQUFBO0VBQ0EsbUJBQUE7RUFDQSxZQUFBO0VBQ0Esa0JBQUE7RUFFQSxpQkFBQTtFQUNBLHFCQUFBO0FBTFI7QUFPUTtFQUNJLFVBQUE7QUFMWjtBQWNRO0VBQ0ksV0FBQTtFQUNBLGFBQUE7RUFDQSxnQkFBQTtFQUNBLGNEekNHO0FDNkJmO0FBZVE7RUFDSSxzQkFBQTtFQUNBLHlCQUFBO0FBYlo7QUFnQlE7RUFDSSxzQkFBQTtFQUNBLHlCQUFBO0FBZFo7QUFpQlE7RUFDSSxzQkFBQTtFQUNBLHlCQUFBO0FBZlo7QUFrQlE7RUFDSSxzQkFBQTtFQUNBLHlCQUFBO0FBaEJaO0FBbUJRO0VBQ0ksa0JBQUE7RUFDQSxVQUFBO0VBQ0EsV0FBQTtFQUNBLGlCQUFBO0VBQ0EsZUFBQTtBQWpCWjtBQW1CWTtFQUNJLGlCQUFBO0VBQ0EsbUJBQUE7QUFqQmhCIiwiZmlsZSI6InNyYy9hcHAvc2hhcmVkL2FsZXJ0L2FsZXJ0LmNvbXBvbmVudC5zY3NzIiwic291cmNlc0NvbnRlbnQiOlsiLyogYmFzZSBjb2xvcnMgKi9cclxuXHJcbiRjb2xvcl9ncmV5XzE6ICMwZDBkMGQ7IFxyXG4kY29sb3JfZ3JleV8yOiAjMzMzMzMzOyBcclxuJGNvbG9yX2dyZXlfMzogIzRkNGQ0ZDsgXHJcbiRjb2xvcl9ncmV5XzQ6ICM2NjY7XHJcbiRjb2xvcl9ncmV5XzU6ICNiMmIyYjI7XHJcbiRjb2xvcl9ncmV5XzY6ICNkOWQ5ZDk7XHJcbiRjb2xvcl9ncmV5XzY6ICNmNWY1ZjU7ICBcclxuXHJcbiRjb2xvcl9ibHVlXzE6ICMwMDMzNjY7IFxyXG4kY29sb3JfYmx1ZV8yOiAjMDA0Mjg0OyBcclxuJGNvbG9yX2JsdWVfMzogIzAwNTJhNTsgXHJcbiRjb2xvcl9ibHVlXzQ6ICM5OWNjZmY7IFxyXG4kY29sb3JfYmx1ZV81OiAjZjVmYWZmOyBcclxuXHJcbiRjb2xvcl9ncmVlbl8xOiAjMTgzNTE4OyBcclxuJGNvbG9yX2dyZWVuXzI6ICMzYTgyM2E7IFxyXG4kY29sb3JfZ3JlZW5fMzogI2I5ZGZiOTsgXHJcbiRjb2xvcl9ncmVlbl80OiAjZWRmN2VkOyBcclxuXHJcbiRjb2xvcl9yZWRfMTogIzY2MDAwYTsgXHJcbiRjb2xvcl9yZWRfMjogI2Q1MjMzZjsvLyNhODAwMTE7IFxyXG4kY29sb3JfcmVkXzM6ICNmZmIyYmE7IFxyXG4kY29sb3JfcmVkXzQ6ICNmZmYwZjE7XHJcblxyXG4kY29sb3JfaW5mXzE6ICMwNDQzNjI7IFxyXG4kY29sb3JfaW5mXzI6ICMwNjVhODQ7IFxyXG4kY29sb3JfaW5mXzM6ICNiNWU1ZmM7IFxyXG4kY29sb3JfaW5mXzQ6ICNmNWZiZmY7XHJcblxyXG4kY29sb3Jfd2FybmluZ18xOiAjNTc0MTAwOyBcclxuJGNvbG9yX3dhcm5pbmdfMjogI2U1YWMwMDsgXHJcbiRjb2xvcl93YXJuaW5nXzM6ICNmZmRmODA7IFxyXG4kY29sb3Jfd2FybmluZ180OiAjZmZmOWU1O1xyXG5cclxuJGNvbnRyYXN0X2JhY2tncm91bnVkOiAjMGQwZDBkO1xyXG4kY29udHJhc3RfZm9udDogI2ZmZjcwMDtcclxuJGNvbnRyYXN0X2xpbms6ICNmZmY7XHJcblxyXG4iLCJAaW1wb3J0ICcuLy4uLy4uLy4uL3N0eWxlcy9jb2xvcnMuc2Nzcyc7XHJcblxyXG5cclxuLmFsZXJ0LXdyYXBlciB7XHJcblxyXG4gICAgcG9zaXRpb246IGFic29sdXRlO1xyXG4gICAgbWFyZ2luLXRvcDogMTUwcHg7XHJcbiAgICB3aWR0aDogMTAwJTtcclxuICAgIHotaW5kZXg6IDEwMDtcclxuICAgIHRyYW5zaXRpb246IGFsbCAuM3MgZWFzZS1pbi1vdXQgIWltcG9ydGFudDtcclxuXHJcbiAgICAuYWxlcnQtYm9keSB7XHJcbiAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlO1xyXG4gICAgICAgIHRvcDogMHB4O1xyXG4gICAgICAgIHdpZHRoOiAxMDAlO1xyXG4gICAgICAgIGNvbG9yOiAkY29sb3JfZ3JleV8xO1xyXG4gICAgICAgIFxyXG5cclxuICAgICAgICB6LWluZGV4OiAxO1xyXG4gICAgICAgIGRpc3BsYXk6IGZsZXg7XHJcbiAgICAgICAgZmxleC1mbG93OiBjb2x1bW47XHJcbiAgICAgICAganVzdGlmeS1jb250ZW50OiBjZW50ZXI7XHJcbiAgICAgICAgYWxpZ24taXRlbXM6IGNlbnRlcjtcclxuICAgICAgICBoZWlnaHQ6IDUycHg7XHJcbiAgICAgICAgbWFyZ2luLWJvdHRvbTogMnB4OyAgICAgICAgICAgICBcclxuICAgICAgICAvLyB0cmFuc2l0aW9uOiBhbGwgLjFzIGVhc2UtaW47XHJcbiAgICAgICAgYm94LXNoYWRvdzogdW5zZXQ7XHJcbiAgICAgICAgbGV0dGVyLXNwYWNpbmc6IC41cHg7XHJcbiAgICBcclxuICAgICAgICAmOmxhc3Qtb2YtdHlwZSB7XHJcbiAgICAgICAgICAgIHotaW5kZXg6IDI7XHJcbiAgICAgICAgICAgIC8vIGJveC1zaGFkb3c6IDBweCAxMHB4IDE1cHggLTEwcHggcmdiYSgwLCAwLCAwLCAwLjIpO1xyXG4gICAgICAgIH1cclxuXHJcbiAgICAgICAgLnRpdGxlIHtcclxuICAgICAgICAgICAgLy8gZm9udC1zaXplOiAwLjlyZW07XHJcbiAgICAgICAgICAgIC8vIG1hcmdpbjogMHB4O1xyXG4gICAgICAgIH1cclxuICAgIFxyXG4gICAgICAgIC5tZXNzYWdlIHtcclxuICAgICAgICAgICAgd2lkdGg6IDEwMCU7XHJcbiAgICAgICAgICAgIHBhZGRpbmc6IDE1cHg7XHJcbiAgICAgICAgICAgIHRleHQtYWxpZ246IGxlZnQ7XHJcbiAgICAgICAgICAgIGNvbG9yOiAkY29sb3JfZ3JleV8xO1xyXG4gICAgICAgIH1cclxuICAgIFxyXG4gICAgICAgICYuaW5mbyB7XHJcbiAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6ICNmZmY7XHJcbiAgICAgICAgICAgIGJvcmRlcjogMnB4IHNvbGlkICRjb2xvcl9pbmZfMjsgICAgICBcclxuICAgICAgICB9ICBcclxuICAgIFxyXG4gICAgICAgICYuc3VjY2VzcyB7XHJcbiAgICAgICAgICAgIGJhY2tncm91bmQtY29sb3I6ICNmZmY7XHJcbiAgICAgICAgICAgIGJvcmRlcjogMnB4IHNvbGlkICRjb2xvcl9ncmVlbl8yOyAgICAgIFxyXG4gICAgICAgIH1cclxuICAgIFxyXG4gICAgICAgICYuZGFuZ2VyIHtcclxuICAgICAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogI2ZmZjtcclxuICAgICAgICAgICAgYm9yZGVyOiAycHggc29saWQgJGNvbG9yX3JlZF8yO1xyXG4gICAgICAgIH0gIFxyXG4gICAgXHJcbiAgICAgICAgJi53YXJuaW5nIHtcclxuICAgICAgICAgICAgYmFja2dyb3VuZC1jb2xvcjogI2ZmZjtcclxuICAgICAgICAgICAgYm9yZGVyOiAycHggc29saWQgJGNvbG9yX3dhcm5pbmdfMjtcclxuICAgICAgICB9XHJcbiAgICBcclxuICAgICAgICAuY2xvc2UtYWxlcnQge1xyXG4gICAgICAgICAgICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbiAgICAgICAgICAgIHJpZ2h0OiAwcHg7XHJcbiAgICAgICAgICAgIHdpZHRoOiA1MHB4O1xyXG4gICAgICAgICAgICBib3gtc2hhZG93OiB1bnNldDtcclxuICAgICAgICAgICAgY3Vyc29yOiBwb2ludGVyO1xyXG5cclxuICAgICAgICAgICAgZGl2e1xyXG4gICAgICAgICAgICAgICAgdGV4dC1hbGlnbjogcmlnaHQ7XHJcbiAgICAgICAgICAgICAgICBwYWRkaW5nLXJpZ2h0OiAxNXB4O1xyXG4gICAgICAgICAgICB9XHJcbiAgICAgICAgfVxyXG4gICAgfSBcclxuXHJcbn1cclxuIl19 */"] });
AlertComponent.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: AlertComponent, factory: AlertComponent.ɵfac, providedIn: 'root' });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](AlertComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'alert',
                templateUrl: './alert.component.html',
                styleUrls: ['./alert.component.scss']
            }]
    }, {
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Injectable"],
        args: [{
                providedIn: 'root',
            }]
    }], function () { return [{ type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ElementRef"] }, { type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Renderer2"] }]; }, { alertConf: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Input"]
        }], closeAlertTime: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
        }], closedAlert: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Output"]
        }], alert: [{
            type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewChild"],
            args: ['alert', { static: false }]
        }] }); })();


/***/ }),

/***/ "./src/app/shared/fullsize-loader/fullsize-loader.component.ts":
/*!*********************************************************************!*\
  !*** ./src/app/shared/fullsize-loader/fullsize-loader.component.ts ***!
  \*********************************************************************/
/*! exports provided: FullsizeLoaderComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "FullsizeLoaderComponent", function() { return FullsizeLoaderComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");


class FullsizeLoaderComponent {
    constructor() { }
    ngOnInit() {
    }
}
FullsizeLoaderComponent.ɵfac = function FullsizeLoaderComponent_Factory(t) { return new (t || FullsizeLoaderComponent)(); };
FullsizeLoaderComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: FullsizeLoaderComponent, selectors: [["fullsize-loader"]], decls: 6, vars: 0, consts: [[1, "overlay"], [1, "loader"]], template: function FullsizeLoaderComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](0, "div", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementStart"](1, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](2, "div");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](3, "div");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](4, "div");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](5, "div");
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementEnd"]();
    } }, styles: [".overlay[_ngcontent-%COMP%] {\n  position: fixed;\n  width: 100%;\n  height: 100%;\n  background: rgba(255, 255, 255, 0.5);\n  z-index: 999;\n}\n.overlay[_ngcontent-%COMP%]   .loader[_ngcontent-%COMP%] {\n  display: inline-block;\n  position: relative;\n  width: 80px;\n  height: 80px;\n  position: absolute;\n  top: 50%;\n  left: 50%;\n  transform: translate(-50%, -50%);\n}\n.overlay[_ngcontent-%COMP%]   .loader[_ngcontent-%COMP%]   div[_ngcontent-%COMP%] {\n  box-sizing: border-box;\n  display: block;\n  position: absolute;\n  width: 64px;\n  height: 64px;\n  margin: 8px;\n  border: 8px solid #0052a5;\n  border-radius: 50%;\n  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;\n  border-color: #0052a5 transparent transparent transparent;\n}\n.overlay[_ngcontent-%COMP%]   .loader[_ngcontent-%COMP%]   div[_ngcontent-%COMP%]:nth-child(1) {\n  animation-delay: -0.45s;\n}\n.overlay[_ngcontent-%COMP%]   .loader[_ngcontent-%COMP%]   div[_ngcontent-%COMP%]:nth-child(2) {\n  animation-delay: -0.3s;\n}\n.overlay[_ngcontent-%COMP%]   .loader[_ngcontent-%COMP%]   div[_ngcontent-%COMP%]:nth-child(3) {\n  animation-delay: -0.15s;\n}\n@keyframes lds-ring {\n  0% {\n    transform: rotate(0deg);\n  }\n  100% {\n    transform: rotate(360deg);\n  }\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9hcHAvc2hhcmVkL2Z1bGxzaXplLWxvYWRlci9mdWxsc2l6ZS1sb2FkZXIuY29tcG9uZW50LnNjc3MiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7RUFFSSxlQUFBO0VBQ0EsV0FBQTtFQUNBLFlBQUE7RUFDQSxvQ0FBQTtFQUNBLFlBQUE7QUFBSjtBQUdJO0VBQ0kscUJBQUE7RUFDQSxrQkFBQTtFQUNBLFdBQUE7RUFDQSxZQUFBO0VBQ0Esa0JBQUE7RUFDQSxRQUFBO0VBQ0EsU0FBQTtFQUNBLGdDQUFBO0FBRFI7QUFHUTtFQUNJLHNCQUFBO0VBQ0EsY0FBQTtFQUNBLGtCQUFBO0VBQ0EsV0FBQTtFQUNBLFlBQUE7RUFDQSxXQUFBO0VBQ0EseUJBQUE7RUFDQSxrQkFBQTtFQUNBLDhEQUFBO0VBQ0EseURBQUE7QUFEWjtBQUlVO0VBQ0UsdUJBQUE7QUFGWjtBQUtVO0VBQ0Usc0JBQUE7QUFIWjtBQU1VO0VBQ0UsdUJBQUE7QUFKWjtBQVFNO0VBQ0U7SUFDRSx1QkFBQTtFQU5SO0VBUU07SUFDRSx5QkFBQTtFQU5SO0FBQ0YiLCJmaWxlIjoic3JjL2FwcC9zaGFyZWQvZnVsbHNpemUtbG9hZGVyL2Z1bGxzaXplLWxvYWRlci5jb21wb25lbnQuc2NzcyIsInNvdXJjZXNDb250ZW50IjpbIi5vdmVybGF5e1xyXG5cclxuICAgIHBvc2l0aW9uOiBmaXhlZDtcclxuICAgIHdpZHRoOjEwMCU7XHJcbiAgICBoZWlnaHQ6MTAwJTtcclxuICAgIGJhY2tncm91bmQ6cmdiYSgyNTUsMjU1LDI1NSwgMC41ICk7XHJcbiAgICB6LWluZGV4OiA5OTk7XHJcbiAgICBcclxuXHJcbiAgICAubG9hZGVyIHtcclxuICAgICAgICBkaXNwbGF5OiBpbmxpbmUtYmxvY2s7XHJcbiAgICAgICAgcG9zaXRpb246IHJlbGF0aXZlO1xyXG4gICAgICAgIHdpZHRoOiA4MHB4O1xyXG4gICAgICAgIGhlaWdodDogODBweDtcclxuICAgICAgICBwb3NpdGlvbjogYWJzb2x1dGU7XHJcbiAgICAgICAgdG9wOiA1MCU7XHJcbiAgICAgICAgbGVmdDogNTAlO1xyXG4gICAgICAgIHRyYW5zZm9ybTogdHJhbnNsYXRlKC01MCUsIC01MCUpO1xyXG4gICAgXHJcbiAgICAgICAgZGl2IHtcclxuICAgICAgICAgICAgYm94LXNpemluZzogYm9yZGVyLWJveDtcclxuICAgICAgICAgICAgZGlzcGxheTogYmxvY2s7XHJcbiAgICAgICAgICAgIHBvc2l0aW9uOiBhYnNvbHV0ZTtcclxuICAgICAgICAgICAgd2lkdGg6IDY0cHg7XHJcbiAgICAgICAgICAgIGhlaWdodDogNjRweDtcclxuICAgICAgICAgICAgbWFyZ2luOiA4cHg7XHJcbiAgICAgICAgICAgIGJvcmRlcjogOHB4IHNvbGlkICMwMDUyYTU7XHJcbiAgICAgICAgICAgIGJvcmRlci1yYWRpdXM6IDUwJTtcclxuICAgICAgICAgICAgYW5pbWF0aW9uOiBsZHMtcmluZyAxLjJzIGN1YmljLWJlemllcigwLjUsIDAsIDAuNSwgMSkgaW5maW5pdGU7XHJcbiAgICAgICAgICAgIGJvcmRlci1jb2xvcjogIzAwNTJhNSB0cmFuc3BhcmVudCB0cmFuc3BhcmVudCB0cmFuc3BhcmVudDtcclxuICAgICAgICAgIH1cclxuICAgIFxyXG4gICAgICAgICAgZGl2Om50aC1jaGlsZCgxKSB7XHJcbiAgICAgICAgICAgIGFuaW1hdGlvbi1kZWxheTogLTAuNDVzO1xyXG4gICAgICAgICAgfVxyXG4gICAgXHJcbiAgICAgICAgICBkaXY6bnRoLWNoaWxkKDIpIHtcclxuICAgICAgICAgICAgYW5pbWF0aW9uLWRlbGF5OiAtMC4zcztcclxuICAgICAgICAgIH1cclxuICAgIFxyXG4gICAgICAgICAgZGl2Om50aC1jaGlsZCgzKSB7XHJcbiAgICAgICAgICAgIGFuaW1hdGlvbi1kZWxheTogLTAuMTVzO1xyXG4gICAgICAgICAgfVxyXG4gICAgICB9XHJcbiAgICBcclxuICAgICAgQGtleWZyYW1lcyBsZHMtcmluZyB7XHJcbiAgICAgICAgMCUge1xyXG4gICAgICAgICAgdHJhbnNmb3JtOiByb3RhdGUoMGRlZyk7XHJcbiAgICAgICAgfVxyXG4gICAgICAgIDEwMCUge1xyXG4gICAgICAgICAgdHJhbnNmb3JtOiByb3RhdGUoMzYwZGVnKTtcclxuICAgICAgICB9XHJcbiAgICAgIH1cclxuXHJcbn1cclxuXHJcblxyXG5cclxuXHJcbiAgIl19 */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵsetClassMetadata"](FullsizeLoaderComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"],
        args: [{
                selector: 'fullsize-loader',
                templateUrl: './fullsize-loader.component.html',
                styleUrls: ['./fullsize-loader.component.scss']
            }]
    }], function () { return []; }, null); })();


/***/ }),

/***/ "./src/app/table-list/table-list.component.ts":
/*!****************************************************!*\
  !*** ./src/app/table-list/table-list.component.ts ***!
  \****************************************************/
/*! exports provided: TableListComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "TableListComponent", function() { return TableListComponent; });
/* harmony import */ var tslib__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! tslib */ "./node_modules/tslib/tslib.es6.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @ng-bootstrap/ng-bootstrap */ "./node_modules/@ng-bootstrap/ng-bootstrap/__ivy_ngcc__/fesm2015/ng-bootstrap.js");
/* harmony import */ var _services_api_service__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./../services/api.service */ "./src/app/services/api.service.ts");
/* harmony import */ var _services_state_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./../services/state.service */ "./src/app/services/state.service.ts");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/__ivy_ngcc__/fesm2015/router.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/__ivy_ngcc__/fesm2015/common.js");
/* harmony import */ var _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../main-header/main-header.component */ "./src/app/main-header/main-header.component.ts");
/* harmony import */ var _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../shared/fullsize-loader/fullsize-loader.component */ "./src/app/shared/fullsize-loader/fullsize-loader.component.ts");










function TableListComponent_fullsize_loader_0_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](0, "fullsize-loader");
} }
function TableListComponent_div_10_tr_10_Template(rf, ctx) { if (rf & 1) {
    const _r13 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "tr");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "td", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "td", 20);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpipe"](5, "date");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](6, "td", 21);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](7, "div", 22);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](8, "button", 23);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function TableListComponent_div_10_tr_10_Template_button_click_8_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r13); const msigRow_r10 = ctx.$implicit; const ctx_r12 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2); const _r2 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵreference"](12); return ctx_r12.showModalDetails(_r2, msigRow_r10.id); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](9, " Szczeg\u00F3\u0142y ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](10, "a", 24);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](11, "svg", 25);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](12, "path", 26);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](13, "path", 27);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](14, " Pobierz");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} if (rf & 2) {
    const msigRow_r10 = ctx.$implicit;
    const ctx_r4 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate1"](" ", msigRow_r10 == null ? null : msigRow_r10.monitorNumber, " ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpipeBind2"](5, 4, msigRow_r10.dateOfPublication, "yyyy-LL-dd"));
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](6);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpropertyInterpolate2"]("href", "", ctx_r4.apiURL, "/Monitor/Download?id=", msigRow_r10.id, "&fileId=false", _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsanitizeUrl"]);
} }
function TableListComponent_div_10_div_12_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 28);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](1, "strona ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](2, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](4, " z ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](5, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](6);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r5 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r5.msigList.page);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](3);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r5.countPages);
} }
function TableListComponent_div_10_div_14_Template(rf, ctx) { if (rf & 1) {
    const _r15 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 29);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("keyup.enter", function TableListComponent_div_10_div_14_Template_div_keyup_enter_0_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r15); const ctx_r14 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2); return ctx_r14.changePage("prev"); })("click", function TableListComponent_div_10_div_14_Template_div_click_0_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r15); const ctx_r16 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2); return ctx_r16.changePage("prev"); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "svg", 30);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](2, "path", 5);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](3, " Poprzednia");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} }
function TableListComponent_div_10_div_15_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 31);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](1, "Poprzednia");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} }
function TableListComponent_div_10_div_16_Template(rf, ctx) { if (rf & 1) {
    const _r18 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 32);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("keyup.enter", function TableListComponent_div_10_div_16_Template_div_keyup_enter_0_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r18); const ctx_r17 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2); return ctx_r17.changePage("next"); })("click", function TableListComponent_div_10_div_16_Template_div_click_0_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r18); const ctx_r19 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2); return ctx_r19.changePage("next"); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](1, "Nast\u0119pna ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](2, "svg", 33);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](3, "path", 34);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} }
function TableListComponent_div_10_div_17_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 31);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](1, "Nast\u0119pna");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} }
function TableListComponent_div_10_Template(rf, ctx) { if (rf & 1) {
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 9);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "table", 10);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](2, "thead", 11);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "tr");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](4, "th", 12);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](5, "Numer monitora");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](6, "th", 12);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](7, "Data");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](8, "th", 12);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](9, "tbody");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](10, TableListComponent_div_10_tr_10_Template, 15, 7, "tr", 13);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](11, "div", 14);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](12, TableListComponent_div_10_div_12_Template, 7, 2, "div", 15);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](13, "div", 16);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](14, TableListComponent_div_10_div_14_Template, 4, 0, "div", 17);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](15, TableListComponent_div_10_div_15_Template, 2, 0, "div", 18);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](16, TableListComponent_div_10_div_16_Template, 4, 0, "div", 19);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](17, TableListComponent_div_10_div_17_Template, 2, 0, "div", 18);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r1 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](10);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngForOf", ctx_r1.msigList == null ? null : ctx_r1.msigList.list);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx_r1.countPages);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx_r1.hidePrev);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", !ctx_r1.hidePrev);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx_r1.hideNext);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](1);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", !ctx_r1.hideNext);
} }
function TableListComponent_ng_template_11_div_0_Template(rf, ctx) { if (rf & 1) {
    const _r24 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](0, "div", 45);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "h4", 46);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](4, "Numer og\u0142oszenia: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](5, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](6);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](7, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](8, "Sygnatura sprawy: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](9, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](10);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](11, "button", 47);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function TableListComponent_ng_template_11_div_0_Template_button_click_11_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r24); const modal_r20 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]().$implicit; return modal_r20.dismiss("Cross click"); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](12, "span", 48);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](13, "\u00D7");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r21 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate1"]("", ctx_r21.monitorDetails == null ? null : ctx_r21.monitorDetails.entityName, " ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r21.monitorDetails == null ? null : ctx_r21.monitorDetails.numberOfNotice);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r21.monitorDetails == null ? null : ctx_r21.monitorDetails.signatureOfCase);
} }
function TableListComponent_ng_template_11_Template(rf, ctx) { if (rf & 1) {
    const _r28 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵgetCurrentView"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](0, TableListComponent_ng_template_11_div_0_Template, 14, 3, "div", 35);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "div", 36);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](2, "div");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](4, "KRS: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](5, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](6);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](7, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](8, "NIP: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](9, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](10);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](11, "br");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](12, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](13, "Numer strony: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](14, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](15);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](16, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](17, "Rozdzia\u0142/nazwa rozdzia\u0142u: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](18, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](19);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](20, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](21, "Nr monitora: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](22, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](23);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](24, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](25, "Data publikacji: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](26, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](27);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpipe"](28, "date");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](29, "div", 37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](30, "Tre\u015B\u0107 nag\u0142\u00F3wka: ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](31, "span");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](32);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](33, "div", 38);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](34, "label", 39);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](35, "Tre\u015B\u0107 og\u0142oszenia");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](36, "textarea", 40);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](37);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](38, "div", 41);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](39, "button", 42);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function TableListComponent_ng_template_11_Template_button_click_39_listener() { const modal_r20 = ctx.$implicit; return modal_r20.close("Close click"); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](40, " Zamknij ");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](41, "a", 43);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](42, "svg", 25);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](43, "path", 26);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](44, "path", 27);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](45, " Pobierz");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceHTML"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](46, "button", 44);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function TableListComponent_ng_template_11_Template_button_click_46_listener() { const modal_r20 = ctx.$implicit; return modal_r20.close("Close click"); })("click", function TableListComponent_ng_template_11_Template_button_click_46_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r28); const ctx_r27 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](); const _r2 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵreference"](12); return ctx_r27.showModalDetails(_r2, ctx_r27.nextPrevIdsObj.prev); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](47, "Poprzedni");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](48, "button", 44);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵlistener"]("click", function TableListComponent_ng_template_11_Template_button_click_48_listener() { const modal_r20 = ctx.$implicit; return modal_r20.close("Close click"); })("click", function TableListComponent_ng_template_11_Template_button_click_48_listener() { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵrestoreView"](_r28); const ctx_r30 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"](); const _r2 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵreference"](12); return ctx_r30.showModalDetails(_r2, ctx_r30.nextPrevIdsObj.next); });
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](49, "Nast\u0119pny");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
} if (rf & 2) {
    const ctx_r3 = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnextContext"]();
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx_r3.monitorDetails);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](6);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.krs);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.nip);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.page);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.chapterName);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.monitorNumber);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpipeBind2"](28, 13, ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.dateOfPublication, "yyyy-LL-dd"));
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate"](ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.textInPosition);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtextInterpolate1"]("              ", ctx_r3.monitorDetails == null ? null : ctx_r3.monitorDetails.textInBody, "");
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpropertyInterpolate2"]("href", "", ctx_r3.apiURL, "/Monitor/Download?id=", ctx_r3.monitorDetails.id, "&fileId=false", _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsanitizeUrl"]);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](5);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("disabled", !ctx_r3.nextPrevIdsObj.prev);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](2);
    _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("disabled", !ctx_r3.nextPrevIdsObj.next);
} }
const _c0 = function () { return [""]; };
class TableListComponent {
    constructor(modalService, api, state, router) {
        this.modalService = modalService;
        this.api = api;
        this.state = state;
        this.router = router;
        this.fullsizeLoader = false;
        this.alertWarning = false;
        this.hideNext = true;
        this.hidePrev = false;
        this.nextPrevIdsObj = {
            prev: false,
            current: false,
            next: false
        };
    }
    ngOnInit() {
        this.state.url$.subscribe({
            next: url => {
                this.apiURL = url;
            }
        });
        this.state.searchRequest$.subscribe({
            next: res => {
                this.request = res;
            }
        });
        this.showData();
    }
    monitorCount() {
        this.allPagesSubscription = this.api.searchMonitorCount(this.request).subscribe({
            next: res => {
                this.countPages = res;
                this.hideNext = this.countPages > this.msigList.page;
                this.hidePrev = this.msigList.page > 1;
            },
            error: err => {
                this.state.shareAlertBody([{
                        status: 'danger',
                        message: err.error.title,
                        alwaysVisible: false
                    }]);
            }
        });
    }
    ngOnDestroy() {
        if (this.monitorDetailsSubscription) {
            this.monitorDetailsSubscription.unsubscribe();
        }
        if (this.allPagesSubscription) {
            this.allPagesSubscription.unsubscribe();
        }
        if (this.serachSubscription) {
            this.serachSubscription.unsubscribe();
        }
        if (this.dataSubscription) {
            this.dataSubscription.unsubscribe();
        }
    }
    prevNextIdsModal(id) {
        this.msigList.list.forEach((el, i) => {
            if (el.id == id) {
                this.nextPrevIdsObj.current = id;
                // this.nextPrevIdsObj = '';
                if (i == 0 && this.msigList.list.length == 1) {
                    this.nextPrevIdsObj.prev = false;
                    this.nextPrevIdsObj.next = false;
                }
                else if (i == 0) {
                    this.nextPrevIdsObj.next = this.msigList.list[i + 1].id;
                    this.nextPrevIdsObj.prev = false;
                }
                else if (i > 0 && (i < this.msigList.list.length - 1)) {
                    this.nextPrevIdsObj.next = this.msigList.list[i + 1].id;
                    this.nextPrevIdsObj.prev = this.msigList.list[i - 1].id;
                }
                else if (i == this.msigList.list.length - 1) {
                    this.nextPrevIdsObj.next = false;
                    this.nextPrevIdsObj.prev = this.msigList.list[i - 1].id;
                }
            }
        });
    }
    showModalDetails(content, id) {
        this.fullsizeLoader = true;
        //this.monitorDetails = null;
        if (id == 0 || id == null) {
            this.state.shareAlertBody([{
                    status: 'warning',
                    message: 'The value "null" is not valid.',
                    alwaysVisible: false
                }]);
            this.fullsizeLoader = false;
        }
        else {
            this.monitorDetailsSubscription = this.api.getMonitorDetails(id).subscribe({
                next: res => {
                    this.fullsizeLoader = false;
                    this.monitorDetails = res;
                    this.prevNextIdsModal(id);
                    this.modalService.open(content, { centered: true, size: 'xl' });
                },
                error: err => {
                    this.fullsizeLoader = false;
                },
                complete: () => {
                    this.fullsizeLoader = false;
                }
            });
        }
    }
    downloadMonitor(id) {
        this.api.getFileMonitor(id).subscribe({
            next: res => {
                let filename = res.headers.get('content-disposition').split("filename=")[1].split(".")[0];
                let dataType = res.body.type;
                let binaryData = [];
                binaryData.push(res.body);
                let downloadLink = document.createElement('a');
                downloadLink.href = window.URL.createObjectURL(new Blob(binaryData, { type: dataType }));
                if (filename)
                    downloadLink.setAttribute('download', filename);
                document.body.appendChild(downloadLink);
                downloadLink.click();
            },
            error: err => {
                console.log(err);
            }
        });
    }
    download(id) {
        return Object(tslib__WEBPACK_IMPORTED_MODULE_0__["__awaiter"])(this, void 0, void 0, function* () {
            try {
                const res = yield this.api.getFileMonitor(id);
                this.downloadFile(res);
            }
            catch (e) {
            }
        });
    }
    downloadFile(data) {
        const url = window.URL.createObjectURL(data);
        window.open(url);
    }
    showData() {
        this.dataSubscription = this.state.data$.subscribe({
            next: res => {
                if (!res) {
                    this.router.navigateByUrl('/');
                }
                else {
                    this.msigList = res;
                    this.monitorCount();
                }
            }
        });
    }
    changePage(action) {
        if (action == "next") {
            this.request.page = this.request.page + 1;
        }
        if (action == "prev" && this.request.page > 1) {
            this.request.page = this.request.page - 1;
        }
        this.fullsizeLoader = true;
        this.serachSubscription = this.api.searchMonitor(this.request).subscribe({
            next: res => {
                this.fullsizeLoader = false;
                let data = res;
                if (data.list.length > 0) {
                    this.state.shareData(res);
                }
            },
            error: err => {
                this.fullsizeLoader = false;
                this.state.shareAlertBody([{
                        status: 'danger',
                        message: err.error.title,
                        alwaysVisible: false
                    }]);
            }
        });
        this.monitorCount();
    }
}
TableListComponent.ɵfac = function TableListComponent_Factory(t) { return new (t || TableListComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_2__["NgbModal"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_services_api_service__WEBPACK_IMPORTED_MODULE_3__["ApiService"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_services_state_service__WEBPACK_IMPORTED_MODULE_4__["StateService"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_router__WEBPACK_IMPORTED_MODULE_5__["Router"])); };
TableListComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineComponent"]({ type: TableListComponent, selectors: [["table-list"]], decls: 13, vars: 4, consts: [[4, "ngIf"], [1, "subTitle", "px-3", "mb-3"], [1, "fluid-container", "d-flex", "flex-wrap", "justify-content-start"], ["role", "link", "aria-label", "Powr\u00F3t do ekranu g\u0142\u00F3wnego", 1, "arrow-back", 3, "routerLink"], ["xmlns", "http://www.w3.org/2000/svg", "width", "18", "height", "18", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-chevron-left"], ["fill-rule", "evenodd", "d", "M11.354 1.646a.5.5 0 0 1 0 .708L5.707 8l5.647 5.646a.5.5 0 0 1-.708.708l-6-6a.5.5 0 0 1 0-.708l6-6a.5.5 0 0 1 .708 0z"], [1, "title"], ["class", "container table-container", "style", "margin-top:75px", 4, "ngIf"], ["content", ""], [1, "container", "table-container", 2, "margin-top", "75px"], [1, "table"], [1, "thead-normal"], ["scope", "col"], [4, "ngFor", "ngForOf"], [1, "d-flex", "justify-content-between", "p-2"], ["class", "pages", 4, "ngIf"], [1, "d-flex", "justify-content-between"], ["tabindex", "0", "class", "btn mr-3 prev p-2", 3, "keyup.enter", "click", 4, "ngIf"], ["style", "color: #888;", "class", "btn mr-3 next p-2", 4, "ngIf"], ["tabindex", "0", "class", "btn mr-3 next p-2", 3, "keyup.enter", "click", 4, "ngIf"], [1, "center-content", 2, "vertical-align", "center"], [1, "center-content"], [1, "d-flex", "flex-wrap", "justify-content-end"], ["type", "button", 1, "btn", "btn-link", "mr-3", "table-action_link", 3, "click"], ["type", "button", "download", "", 1, "btn", "btn-link", "table-action_link", 3, "href"], ["xmlns", "http://www.w3.org/2000/svg", "width", "16", "height", "16", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-download"], ["d", "M.5 9.9a.5.5 0 0 1 .5.5v2.5a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-2.5a.5.5 0 0 1 1 0v2.5a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2v-2.5a.5.5 0 0 1 .5-.5z"], ["d", "M7.646 11.854a.5.5 0 0 0 .708 0l3-3a.5.5 0 0 0-.708-.708L8.5 10.293V1.5a.5.5 0 0 0-1 0v8.793L5.354 8.146a.5.5 0 1 0-.708.708l3 3z"], [1, "pages"], ["tabindex", "0", 1, "btn", "mr-3", "prev", "p-2", 3, "keyup.enter", "click"], ["xmlns", "http://www.w3.org/2000/svg", "width", "16", "height", "16", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-chevron-left"], [1, "btn", "mr-3", "next", "p-2", 2, "color", "#888"], ["tabindex", "0", 1, "btn", "mr-3", "next", "p-2", 3, "keyup.enter", "click"], ["xmlns", "http://www.w3.org/2000/svg", "width", "16", "height", "16", "fill", "currentColor", "viewBox", "0 0 16 16", 1, "bi", "bi-chevron-right"], ["fill-rule", "evenodd", "d", "M4.646 1.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 0 .708l-6 6a.5.5 0 0 1-.708-.708L10.293 8 4.646 2.354a.5.5 0 0 1 0-.708z"], ["class", "modal-header", 4, "ngIf"], [1, "modal-body"], [1, "modal-title_sub"], [1, "mt-4", "mb-2"], ["for", "exampleFormControlInput1", 1, "form-label"], ["id", "exampleFormControlTextarea1", "rows", "8", "readonly", "", "placeholder", "Tre\u015B\u0107", 1, "form-control"], [1, "modal-footer"], ["type", "button", 1, "btn", "btn-secondary", 3, "click"], ["type", "button", "download", "", 1, "btn", "btn-primary", 3, "href"], ["type", "button", 1, "btn", "btn-secondary", 3, "disabled", "click"], [1, "modal-header"], [1, "modal-title"], ["type", "button", "aria-label", "Close", 1, "close", 3, "click"], ["aria-hidden", "true"]], template: function TableListComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](0, TableListComponent_fullsize_loader_0_Template, 1, 0, "fullsize-loader", 0);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](1, "main-header");
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](2, "div", 1);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](3, "div", 2);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](4, "a", 3);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceSVG"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](5, "svg", 4);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelement"](6, "path", 5);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](7, " Wstecz ");
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵnamespaceHTML"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementStart"](8, "div", 6);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtext"](9, " Wynik wyszukiwania ");
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵelementEnd"]();
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](10, TableListComponent_div_10_Template, 18, 6, "div", 7);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](11, TableListComponent_ng_template_11_Template, 50, 16, "ng-template", null, 8, _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplateRefExtractor"]);
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx.fullsizeLoader);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](4);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("routerLink", _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵpureFunction0"](3, _c0));
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵadvance"](6);
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵproperty"]("ngIf", ctx.msigList);
    } }, directives: [_angular_common__WEBPACK_IMPORTED_MODULE_6__["NgIf"], _main_header_main_header_component__WEBPACK_IMPORTED_MODULE_7__["MainHeaderComponent"], _angular_router__WEBPACK_IMPORTED_MODULE_5__["RouterLinkWithHref"], _shared_fullsize_loader_fullsize_loader_component__WEBPACK_IMPORTED_MODULE_8__["FullsizeLoaderComponent"], _angular_common__WEBPACK_IMPORTED_MODULE_6__["NgForOf"]], pipes: [_angular_common__WEBPACK_IMPORTED_MODULE_6__["DatePipe"]], styles: [".center-content[_ngcontent-%COMP%] {\n  padding: 4px 2px !important;\n}\n.modal-title_sub[_ngcontent-%COMP%] {\n  font-size: 1rem;\n  font-weight: 400;\n}\n.modal-title_sub[_ngcontent-%COMP%]   span[_ngcontent-%COMP%] {\n  font-weight: 600;\n}\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbInNyYy9zdHlsZXMvY29sb3JzLnNjc3MiLCJzcmMvYXBwL3RhYmxlLWxpc3QvdGFibGUtbGlzdC5jb21wb25lbnQuc2NzcyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiQUFBQSxnQkFBQTtBQ0VBO0VBQ0ksMkJBQUE7QUFBSjtBQVFBO0VBQ0ksZUFBQTtFQUNBLGdCQUFBO0FBTEo7QUFPSTtFQUNJLGdCQUFBO0FBTFIiLCJmaWxlIjoic3JjL2FwcC90YWJsZS1saXN0L3RhYmxlLWxpc3QuY29tcG9uZW50LnNjc3MiLCJzb3VyY2VzQ29udGVudCI6WyIvKiBiYXNlIGNvbG9ycyAqL1xyXG5cclxuJGNvbG9yX2dyZXlfMTogIzBkMGQwZDsgXHJcbiRjb2xvcl9ncmV5XzI6ICMzMzMzMzM7IFxyXG4kY29sb3JfZ3JleV8zOiAjNGQ0ZDRkOyBcclxuJGNvbG9yX2dyZXlfNDogIzY2NjtcclxuJGNvbG9yX2dyZXlfNTogI2IyYjJiMjtcclxuJGNvbG9yX2dyZXlfNjogI2Q5ZDlkOTtcclxuJGNvbG9yX2dyZXlfNjogI2Y1ZjVmNTsgIFxyXG5cclxuJGNvbG9yX2JsdWVfMTogIzAwMzM2NjsgXHJcbiRjb2xvcl9ibHVlXzI6ICMwMDQyODQ7IFxyXG4kY29sb3JfYmx1ZV8zOiAjMDA1MmE1OyBcclxuJGNvbG9yX2JsdWVfNDogIzk5Y2NmZjsgXHJcbiRjb2xvcl9ibHVlXzU6ICNmNWZhZmY7IFxyXG5cclxuJGNvbG9yX2dyZWVuXzE6ICMxODM1MTg7IFxyXG4kY29sb3JfZ3JlZW5fMjogIzNhODIzYTsgXHJcbiRjb2xvcl9ncmVlbl8zOiAjYjlkZmI5OyBcclxuJGNvbG9yX2dyZWVuXzQ6ICNlZGY3ZWQ7IFxyXG5cclxuJGNvbG9yX3JlZF8xOiAjNjYwMDBhOyBcclxuJGNvbG9yX3JlZF8yOiAjZDUyMzNmOy8vI2E4MDAxMTsgXHJcbiRjb2xvcl9yZWRfMzogI2ZmYjJiYTsgXHJcbiRjb2xvcl9yZWRfNDogI2ZmZjBmMTtcclxuXHJcbiRjb2xvcl9pbmZfMTogIzA0NDM2MjsgXHJcbiRjb2xvcl9pbmZfMjogIzA2NWE4NDsgXHJcbiRjb2xvcl9pbmZfMzogI2I1ZTVmYzsgXHJcbiRjb2xvcl9pbmZfNDogI2Y1ZmJmZjtcclxuXHJcbiRjb2xvcl93YXJuaW5nXzE6ICM1NzQxMDA7IFxyXG4kY29sb3Jfd2FybmluZ18yOiAjZTVhYzAwOyBcclxuJGNvbG9yX3dhcm5pbmdfMzogI2ZmZGY4MDsgXHJcbiRjb2xvcl93YXJuaW5nXzQ6ICNmZmY5ZTU7XHJcblxyXG4kY29udHJhc3RfYmFja2dyb3VudWQ6ICMwZDBkMGQ7XHJcbiRjb250cmFzdF9mb250OiAjZmZmNzAwO1xyXG4kY29udHJhc3RfbGluazogI2ZmZjtcclxuXHJcbiIsIkBpbXBvcnQgXCIuLy4uLy4uL3N0eWxlcy9jb2xvcnMuc2Nzc1wiO1xyXG5cclxuLmNlbnRlci1jb250ZW50IHtcclxuICAgIHBhZGRpbmc6IDRweCAycHggIWltcG9ydGFudDtcclxufVxyXG5cclxuXHJcbi50YWJsZS1hY3Rpb25fbGlua3tcclxuICAgIC8vIGZvbnQtc2l6ZTogMTRweDtcclxufVxyXG5cclxuLm1vZGFsLXRpdGxlX3N1YiB7XHJcbiAgICBmb250LXNpemU6IDFyZW07XHJcbiAgICBmb250LXdlaWdodDogNDAwO1xyXG5cclxuICAgIHNwYW4ge1xyXG4gICAgICAgIGZvbnQtd2VpZ2h0OiA2MDA7XHJcbiAgICB9XHJcbn1cclxuXHJcbi8vIC5hcnJvdy1iYWNrIHtcclxuLy8gICAgIHBhZGRpbmctcmlnaHQ6IDJlbTtcclxuLy8gICAgIG1hcmdpbi1yaWdodDogMmVtO1xyXG4vLyAgICAgYm9yZGVyLXJpZ2h0OiAxcHggc29saWQgI2QxZDFkMTtcclxuLy8gICAgIGFsaWduLXNlbGY6IGNlbnRlcjtcclxuLy8gICAgIGZvbnQtc2l6ZToxcmVtO1xyXG4vLyAgICAgZm9udC13ZWlnaHQ6NjAwO1xyXG4vLyAgICAgY29sb3I6ICRjb2xvcl9ibHVlXzM7XHJcbi8vICAgICBjdXJzb3I6IHBvaW50ZXI7XHJcblxyXG4vLyAgICAgc3ZnIHtcclxuLy8gICAgICAgICBtYXJnaW4tdG9wOiAtMnB4O1xyXG4vLyAgICAgICAgIG1hcmdpbi1yaWdodDogOHB4O1xyXG4vLyAgICAgfVxyXG5cclxuLy8gfVxyXG5cclxuLy8gLnRhYmxlIHRoLCAudGFibGUgdGQge1xyXG4vLyAgICAgcGFkZGluZzogMC40cmVtO1xyXG4vLyAgICAgdmVydGljYWwtYWxpZ246IGNlbnRlciAhaW1wb3J0YW50O1xyXG4vLyAgICAgYm9yZGVyLXRvcDogMXB4IHNvbGlkICNkZWUyZTY7XHJcbi8vIH1cclxuXHJcbi8vIC5wYWdlc3tcclxuLy8gICAgIGNvbG9yOiAkY29sb3JfYmx1ZV8xO1xyXG5cclxuLy8gICAgIHNwYW4ge1xyXG4vLyAgICAgICAgIGZvbnQtd2VpZ2h0OjUwMDtcclxuLy8gICAgICAgICAvLyBjb2xvcjogJGNvbG9yX2JsdWVfMTtcclxuLy8gICAgIH1cclxuLy8gfVxyXG5cclxuLy8gLmJ0bi5wcmV2LCAuYnRuLm5leHQge1xyXG5cclxuLy8gICAgIGNvbG9yOiAkY29sb3JfYmx1ZV8xO1xyXG5cclxuLy8gICAgICY6aG92ZXIge1xyXG4vLyAgICAgICAgIHRleHQtZGVjb3JhdGlvbjogdW5kZXJsaW5lO1xyXG4vLyAgICAgfVxyXG4vLyB9Il19 */"] });
/*@__PURE__*/ (function () { _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵsetClassMetadata"](TableListComponent, [{
        type: _angular_core__WEBPACK_IMPORTED_MODULE_1__["Component"],
        args: [{
                selector: 'table-list',
                templateUrl: './table-list.component.html',
                styleUrls: ['./table-list.component.scss']
            }]
    }], function () { return [{ type: _ng_bootstrap_ng_bootstrap__WEBPACK_IMPORTED_MODULE_2__["NgbModal"] }, { type: _services_api_service__WEBPACK_IMPORTED_MODULE_3__["ApiService"] }, { type: _services_state_service__WEBPACK_IMPORTED_MODULE_4__["StateService"] }, { type: _angular_router__WEBPACK_IMPORTED_MODULE_5__["Router"] }]; }, null); })();


/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
const environment = {
    production: true
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/__ivy_ngcc__/fesm2015/core.js");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/__ivy_ngcc__/fesm2015/platform-browser.js");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_1__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
_angular_platform_browser__WEBPACK_IMPORTED_MODULE_3__["platformBrowser"]().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(err => console.error(err));


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! C:\Users\matbie\source\repos\MS - MSiG 2.0\MSIG FrontOffice\ClientApp\src\main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map