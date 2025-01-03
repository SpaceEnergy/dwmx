const pluginName = "dwmx";
function InitializePlugins() {
    /**
     * This function is called n times depending on n plugin count,
     * Create the plugin list if it wasn't already created
     */
    !window.PLUGIN_LIST && (window.PLUGIN_LIST = {});
    // initialize a container for the plugin
    if (!window.PLUGIN_LIST[pluginName]) {
        window.PLUGIN_LIST[pluginName] = {};
    }
}
InitializePlugins()
const __call_server_method__ = (methodName, kwargs) => Millennium.callServerMethod(pluginName, methodName, kwargs)
const __wrapped_callable__ = (route) => MILLENNIUM_API.callable(__call_server_method__, route)
var millennium_main=function(e,n){"use strict";const o=window.open;return window.open=function(e,n,t,r){if(!e)return o(e,n,t,r);const a=new URL(e),i=a.searchParams;return i.has("createflags")&&"18"===i.get("createflags")&&(i.set("createflags","274"),a.search=i.toString(),e=a.toString()),console.log("open",e),o(e,n,t,r)},e.default=async function(){console.log("loading dwmx"),n.Millennium.exposeObj(e,{})},Object.defineProperty(e,"__esModule",{value:!0}),e}({},window.MILLENNIUM_API);

function ExecutePluginModule() {
    // Assign the plugin on plugin list. 
    Object.assign(window.PLUGIN_LIST[pluginName], millennium_main);
    // Run the rolled up plugins default exported function 
    millennium_main["default"]();
    MILLENNIUM_BACKEND_IPC.postMessage(1, { pluginName: pluginName });
}
ExecutePluginModule()