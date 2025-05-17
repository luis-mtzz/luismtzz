import { Menubar, MenubarMenu, MenubarTrigger, MenubarContent, MenubarItem } from "./ui/menubar";

export default function TopLeftMenuBar() {
    return (
        <Menubar>
            <MenubarMenu>
                <MenubarTrigger>File</MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>New</MenubarItem>
                    <MenubarItem>Open...</MenubarItem>
                    <MenubarItem>Save</MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Stats</MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>Riot</MenubarItem>
                    <MenubarItem>Steam</MenubarItem>
                    <MenubarItem>Music</MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Recipes</MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>View</MenubarItem>
                </MenubarContent>
            </MenubarMenu>
            <MenubarMenu>
                <MenubarTrigger>Profile</MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>View</MenubarItem>
                    <MenubarItem>Edit</MenubarItem>
                </MenubarContent>
            </MenubarMenu>
        </Menubar>
    );
}