from client import LinkedinCarouselGrowthNarrativeGeneratorClient

def main():
    client = LinkedinCarouselGrowthNarrativeGeneratorClient()
    res = client.generate_carousel_slides('The Ultimate Zero-to-One Agentic Workflow Blueprint', 6)
    print('LinkedIn Carousel Generator: ' + res['carousel_generation_id'] + ' (' + str(res['slides_rendered_count']) + ' slides)')
    print('Hook Engagement Score: ' + str(res['hook_engagement_score_pct']) + '% | CTA: ' + str(res['call_to_action_configured']))
    print('Carousel PDF: ' + res['multi_page_pdf_carousel_url'])

if __name__ == '__main__':
    main()
