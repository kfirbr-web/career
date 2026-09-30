# Leap Tools: application questions (draft 1, 2026-09-30)

## 1. What is an app that you love? Why do you love it? What would you change about it? How would you prioritize your proposed changes?

AllTrails. I hike long trails at high altitude and train daily, so I open it before almost every hike. I love it because it answers the one question that matters before a hike, "is this trail right for me today?", with a map, the distance and elevation, and recent photos and reviews from people who were just there. The photos do more than the text. One picture of snow on a pass tells me more than any description.

What I would change:
1. **Current conditions on one screen.** Today I scroll through reviews to piece together snow, mud, or closures. I would summarize the last two weeks of reviews and photos into a short conditions card at the top of the trail page, with the date of each signal.
2. **Time estimates based on my own pace.** The estimate is generic. My recorded hikes already show how fast I climb, so the app could use them.
3. **Planning for multi-day routes.** Splitting a long trail into daily sections, with water and campsites along the way.

How I would prioritize: by how many hikers it helps, how often, and how much it matters for safety, against the effort to build it. Conditions come first: every hiker needs them on every hike, and wrong conditions are a safety risk. The data is already in the app, so the first version is mostly summarizing it. I would ship a simple version, then measure whether people open fewer reviews before starting and report fewer surprises afterwards. Personal pace is second: it helps everyone and uses data the app already has. Multi-day planning is last: it matters a lot to a smaller group, and it is the most work.

## 2. Your changes lead to fewer people changing the size of the product before they add to cart. Keep or revert?

I would not decide on that number alone. Fewer size changes can mean two opposite things. Either the default size is now right more often, so people have less to fix, which is good. Or people are no longer noticing the size selector and are adding the wrong size, which is bad and shows up later as returns and exchanges.

So I would look at what happens after the add to cart:
- Add to cart and purchase conversion. Did they go up?
- Size-related returns and exchanges, and support tickets about size, for orders placed after the change.
- If I can, a quick session review or a few user calls to see if people see the selector at all.

If conversion went up and size-related returns stayed flat, I would keep the change. If returns went up, I would revert or fix it, for example by making the selected size more visible before add to cart. A return costs more than a lost sale.

I have made this kind of call before. When I fixed our login flow, conversion went from 40% to 85%, but I also checked that related support tickets dropped (they fell 90%) before I called it a win. The same question applies to Roomvo: if fewer people change the rug size in the visualizer, is it because the default size fits their room, or because they didn't notice they could change it?

## 3. How does this opportunity fit into your long-term career aspirations?

Long term, I want to lead product for AI and visual products. This role fits that on both counts.

On the AI and visual side, Roomvo's whole product is computer vision and generative AI turned into something a shopper uses in a few taps. That is where I want to go deep. I have prototyped AI features and I build with Claude Code, but I want to work on a product where the AI is the product, not a feature on the side. I also trained as an architect, and I have spent years thinking about how a room looks and feels. A product that puts a rug or a tile into someone's real room brings that background and my product work together.

On leadership: owning a new consumer app from concept to launch is the job I want to grow from. At Bewith I was the company's first PM and launched its first mobile apps. Doing that again with a stronger technology behind it, and growing into leading the consumer product line as it grows, is the path I want.

## 4. What is the most technically complex task you've done? Did you enjoy it?

Rebuilding user access and permissions at Bewith.io. Our clients were municipalities, and every city was organized differently: departments inside departments, staff who needed access to one program but not another, and admins at different levels. The original access model could not represent that, so clients could not roll the platform out to new departments.

I owned the whole access lifecycle, from provisioning to role assignment. I mapped how each city was actually structured, turned that into a roles and permissions model that could handle nested departments, and worked through it with Engineering so it held up across every client on the platform. The hard part was making one model flexible enough for very different org structures without making it confusing for the admins setting it up.

The result: clients could expand into new departments, and contracts grew 100%+ through those expansions.

Did I enjoy it? Yes, a lot. It is the kind of problem I like most: messy real-world structure that has to become clean system logic, and my architecture training helped with it directly.
