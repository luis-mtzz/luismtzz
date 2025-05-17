import { createRouter, createRoute, Outlet, createRootRoute} from "@tanstack/react-router";
import Home from "@/pages/home/Home";

const rootRoute = createRootRoute({
    component: () => <Outlet/>
});

const homeRoute = createRoute({
    getParentRoute: () => rootRoute,
    path: "/",
    component: Home
});

const routeTree = rootRoute.addChildren([homeRoute]);
const router = createRouter({ routeTree })

export default router;