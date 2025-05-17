import TopLeftMenuBar from "@/components/TopLeftMenubar";
import TopRightMenubar from "@/components/TopRightMenubar";
import { Card, CardContent } from "@/components/ui/card";

export default function Home() {
    return (
        <div className="relative min-h-screen bg-background text-foreground">
            <div className="absolute top-0 left-0 m-4">
                <TopLeftMenuBar/>
            </div>
            <div className="absolute top-0 right-0 m-4">
                <TopRightMenubar/>
            </div>
            <div className="flex items-center justify-center min-h-screen pl-4 pr-4">
                <Card className="w-full h-full mx-auto">
                    <CardContent>
                    </CardContent>
                </Card>
            </div>
        </div>
    )
}