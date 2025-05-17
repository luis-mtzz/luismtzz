import { Menubar, MenubarContent, MenubarItem, MenubarMenu, MenubarTrigger} from "./ui/menubar";
import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";

export default function TopRightMenubar() {
    return (
        <Menubar>
            <MenubarMenu>
                <MenubarTrigger className="flex items-center space-x-2">
                    <span>luismtzz</span>
                    <Avatar className="h-6 w-6">
                        <AvatarImage src="https://ddragon.leagueoflegends.com/cdn/15.10.1/img/champion/Vayne.png"/>
                        <AvatarFallback>Vayne</AvatarFallback>
                    </Avatar>
                </MenubarTrigger>
                <MenubarContent>
                    <MenubarItem>Settings</MenubarItem>
                </MenubarContent>
            </MenubarMenu>
        </Menubar>
    )
}