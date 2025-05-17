prompt = """
-> ABC Manufacturing Co. 
Company type: Private joint-stock company 
Sector / industry: Heavy industrial equipment 
-> Need: custom-built factory
Budget: ≈ USD 2 million (turn-key)
Delivery: 12 months
Cash-flow preference: Minimal cash out until factory is operational
"""

# Multi Agents system outputs we got, for caching purposes in the demo
requirements = """
Requirement Sheet                                                                                                                                                                                    
   • Company Profile:                                                                                                                                                                                  
      • Name: ABC Manufacturing Co.                                                                                                                                                                    
      • Company Type: Private joint-stock company                                                                                                                                                      
      • Sector/Industry: Heavy industrial equipment                                                                                                                                                    
   • Financing Need:                                                                                                                                                                                   
      • Asset: Custom-built factory                                                                                                                                                                    
      • Type: Turn-key project                                                                                                                                                                         
      • Budget: Approximately USD 2 million                                                                                                                                                            
   • Timing:                                                                                                                                                                                           
      • Delivery: 12 months                                                                                                                                                                            
   • Cash-Flow Preference:                                                                                                                                                                             
      • Minimal cash out until factory is operational                                                                                                                                                  
                                                                                                                                                                                                       
  Now, I will delegate tasks to the team members to gather more information about specific aspects of the requirements.                                                                                
                                                                                                                                                                                                       
  Okay, it seems like both agents require more information to fulfill their tasks effectively. I will now update the shared context with the information gathered so far and the questions that need   
  to be answered.                                                                                                                                                                                      
                                                                                                                                                                                                       
  Okay, I will now provide a more complete requirement sheet based on the initial information and the questions raised by Agent 2.                                                                     
                                                                                                                                                                                                       
  Requirements Sheet                                                                                                                                                                                   
                                                                                                                                                                                                       
  I. Company Profile                                                                                                                                                                                   
                                                                                                                                                                                                       
   • Legal Type: Private joint-stock company.                                                                                                                                                          
      • Further Clarification Needed: What specific type of joint-stock company? (e.g., In what jurisdiction is it incorporated?)                                                                      
   • Sector/Industry: Heavy industrial equipment                                                                                                                                                       
      • Further Clarification Needed: What specific NAICS code?                                                                                                                                        
   • Years Active: To be determined.                                                                                                                                                                   
      • Further Clarification Needed: How many years has the company been active?                                                                                                                      
   • Governance Notes: To be determined.                                                                                                                                                               
      • Further Clarification Needed: Any specific stakeholders, reporting requirements, or internal approval processes that could impact decision-making speed?                                       
                                                                                                                                                                                                       
  II. Financing Need                                                                                                                                                                                   
                                                                                                                                                                                                       
   • Asset(s) to Purchase/Build: Custom-built factory                                                                                                                                                  
      • Further Clarification Needed: Detailed list of what needs funding.                                                                                                                             
   • CAPEX vs. OPEX: To be determined.                                                                                                                                                                 
      • Further Clarification Needed: Capital expenditure (initial investment) versus operational expenditure (ongoing costs) breakdown.                                                               
   • Budget: ≈ USD 2 million (turn-key)                                                                                                                                                                
      • Further Clarification Needed: Maximum amount available for this project. Is the budget inclusive of all costs (design, permits, construction, equipment, commissioning, contingency)?          
                                                                                                                                                                                                       
  III. Timing                                                                                                                                                                                          
                                                                                                                                                                                                       
   • Delivery: 12 months                                                                                                                                                                               
      • Further Clarification Needed: How flexible is the 12-month target? Are there hard deadlines (contractual obligations, market entry windows)? What penalties are possible for delays?           
   • Milestone Payments: To be determined.                                                                                                                                                             
      • Further Clarification Needed: Preferences for how payments are structured (e.g., based on completion of design, permits, construction phases).                                                 
                                                                                                                                                                                                       
  IV. Cash-Flow Preference                                                                                                                                                                             
                                                                                                                                                                                                       
   • Preference: Minimal cash out until factory is operational. Further Clarification Needed:                                                                                                          
      • Are any grace periods needed for loan repayments?                                                                                                                                              
      • Does the company’s revenue have seasonal peaks and valleys?                                                                                                                                    
      • What is the expected return on investment (ROI) for this factory?                                                                                                                              
                                                                                                                                                                                                       
  V. Risk Considerations                                                                                                                                                                               
                                                                                                                                                                                                       
   • Permitting Delays: Risk of delays in obtaining necessary permits and approvals.                                                                                                                   
   • Construction Delays: Potential delays due to weather, labor shortages, or material supply issues.                                                                                                 
   • Equipment Installation and Commissioning: Risks associated with equipment delivery, installation, and successful commissioning.                                                                   
   • Cost Overruns: Risk of exceeding the allocated budget due to unforeseen expenses or changes in scope.                                                                                             
   • Financing Risks: Changes in interest rates or availability of financing.                                                                                                                          
   • Operational Risks: Risks associated with the factory's ongoing operations, such as equipment failure or production inefficiencies.                                                                
                                                                                                                                                                                                       
  Next Stage Instructions:                                                                                                                                                                             
                                                                                                                                                                                                       
  The next team of agents will map the requirements to Islamic Financial Accounting Standards (FAS). They should pay special attention to:                                                             
                                                                                                                                                                                                       
   1 The murabaha structure and the permissibility of deferred payment arrangements.                                                                                                                   
   2 The istisna'a contract and its suitability for financing the construction of the factory.                                                                                                         
   3 The ijarah structure to determine the viability of an equipment lease agreement.                                                                                                                  
   4 The diminishing musharaka structure to determine the feasibility of a partnership in the factory.                                                                                                 
                                                                                                                                                                                                       
  Specifically, the agents should determine if the minimal cash out preference until the factory is operational is aligned with all Islamic Financial Accounting Standards (FAS).   
"""

mapping = """
                                                                           1. FAS 10 – Istisnaa’ and Parallel Istisnaa’                                                                                                                                                                                                                                                              
Best for: Turn-key, custom-built, manufacturing/construction on order.                                                                                                                             
                                                                                                                                                                                                   
 • Key Mapping:                                                                                                                                                                                    
    • The standard and its accounting treatment sections ([statement_of_standard], [accounting_treatment_seller], [istisnaa_revenue_profit], [deferred_profits], [accounting_treatment_buyer],     
      [receipt_of_al_masnoo]) explicitly allow for payment after completion or through milestone-based instalments.                                                                                
    • "The contract price may be fully paid by the buyer in instalments during the contract based on progress… However, all or part of the price may be paid following completion of the contract."
      ([deferred_profits])                                                                                                                                                                         
    • This flexibility in timing and structure enables minimal or deferred cash outflows until the factory is operational.                                                                         
                                                                                                                                                                                                   
Conclusion:                                                                                                                                                                                        
FAS 10 (Istisnaa’) is the most directly suited standard for a turn-key factory construction, especially if you wish to minimize payments until the asset is operational.                           
                                                                                                                                                                                                   
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                  2. FAS 4 – Musharaka Financing (Diminishing Musharaka variant)                                                                   
                                                                                                                                                                                                   
Best for: Gradual transfer of factory ownership to the client.                                                                                                                                     
                                                                                                                                                                                                   
 • Key Mapping:                                                                                                                                                                                    
    • Diminishing Musharaka is described as a partnership where the financial institution gradually sells its share ([definitions], [accounting_treatment_measurement_diminishing_end_period]),    
      usually tied to instalment payments or buy-out linked to owner's cash flow.                                                                                                                  
    • "The Islamic bank’s share declines as the client’s share increases until the latter becomes sole owner."                                                                                     
    • If structured after construction, the transfer/payments can begin when the asset is generating income, supporting minimal cash out at early stages.                                          
                                                                                                                                                                                                   
Conclusion:                                                                                                                                                                                        
FAS 4 (Diminishing Musharaka) may be used in conjunction with, or following, Istisnaa’—especially effective for post-construction phase financing/ownership transfer, with gradual payments aligned
to operational cash flows.                                                                                                                                                                         
                                                                                                                                                                                                   
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                                                                                                                                   
                                                                                           Summary Table                                                                                           
                                                                                                                                                                                                   
                                                                                                                                                                                                   
  Requirement                         FAS Reference                   Structure                           Minimal Cash Out Supportable?                                                            
 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                                                  
  Custom-built, turn-key factory      FAS 10 (Istisnaa’)              Progressive construction contract   Yes, via deferred/milestone payments                                                     
  Gradual ownership post-completion   FAS 4 (Diminishing Musharaka)   Partnership with staged buyout      Yes, via staged transfers/installments                                                   
                                                                                                                                                                                                   
                                                                                                                                                                                                   
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                                                                                 Special Note on Minimal Cash Out                                                                                  
                                                                                                                                                                                                   
Both FAS 10 and FAS 4 support structures enabling minimal or deferred cash outflows, provided contractual terms are designed accordingly:                                                          
                                                                                                                                                                                                   
 • Istisnaa’ allows project-based, deferred, or completion-linked payments.                                                                                                                        
 • Diminishing Musharaka enables gradual payments tied to income, so buyouts can be staged after the asset becomes productive.                                                                     
                                                                                                                                                                                                   
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
References:                                                                                                                                                                                        
                                                                                                                                                                                                   
 • FAS 10: [statement_of_standard], [deferred_profits], [receipt_of_al_masnoo]                                                                                                                     
 • FAS 4: [definitions], [accounting_treatment_measurement_diminishing_end_period], [accounting_treatment_diminishing_profits_losses]                                                              
                                                                                                                                                                                                   
If you require mapping for Ijarah (equipment leasing) or Murabaha (deferred payment sale), let me know. For your project’s main needs, FAS 10 and FAS 4 are directly applicable and compliant with 
your minimal cash out preference.                                                                                                                                                                  
                                                                                                                                                                         
"""

design = """                                                                                                                                                                      
                                                                        1. Turn-Key Construction Finance (FAS 10: Istisnaa’)                                                                         
                                                                                                                                                                                                     
  • The Islamic financial institution enters into an Istisnaa’ contract with ABC for a custom-built factory.                                                                                         
  • Payment: 100% deferred until project handover or structured in large milestone tranches—enabling minimal cash outlay until operational.                                                          
  • The financier contracts with a builder under a parallel Istisnaa’.                                                                                                                               
  • On delivery, ownership transfers to ABC, triggering payment.                                                                                                                                     
  • Shariah features: no riba, clearly defined specs, transparent milestone/payment schedule.                                                                                                        
  • Useful tags: istisnaa, deferred_payment, milestone_payment, construction_contract, turn_key                                                                                                      
                                                                                                                                                                                                     
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
                                                                                                                                                                                                     
                                                               2. Post-Construction Ownership Transfer (FAS 4: Diminishing Musharaka)                                                                
                                                                                                                                                                                                     
  • After construction, ABC forms a Musharaka partnership with the financier for the completed factory.                                                                                              
  • Financier holds the bulk of shares initially; ABC gradually purchases these shares after the factory becomes operational, using generated cash flow.                                             
  • ABC pays proportional lease/rental on financier’s remaining share during the buyout period.                                                                                                      
  • No buyout/rental outflows required until the factory is operational.                                                                                                                             
  • Shariah features: partnership structure, staged buyback, rentals instead of interest.                                                                                                            
  • Useful tags: diminishing_musharaka, ownership_transfer, staged_buyout, post_construction, minimal_cash_out                                                                                       
                                                                                                                                                                                                     
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
      This dual-phase product fully meets your turn-key delivery, deferred cash out, and gradual post-completion ownership needs—while staying precisely aligned with AAOIFI FAS 10 and FAS 4.       
"""

validation = """
                                                                         1. Turn-Key Construction Finance (Istisnaa, FAS 10)                                                                         
                                                                                                                                                                                                     
 Key Compliance Points:                                                                                                                                                                              
                                                                                                                                                                                                     
  • Istisnaa Structure: Permits custom factory construction with deferred or milestone payments, as long as all triggers are tied to completed, verifiable milestones, not to the mere passage of    
    time.                                                                                                                                                                                            
  • Parallel Istisnaa: Financier may contract in parallel with a builder; these contracts must remain legally and operationally independent.                                                         
  • Ownership Transfer: Must occur only upon completion to spec and handover/acceptance; no premature transfer.                                                                                      
  • No Riba: Payments linked strictly to work/progress, not the use of money or time value.                                                                                                          
  • Contract Clarity: All specs, milestone events, and payment schedules must be explicit and mutually agreed from inception.                                                                        
                                                                                                                                                                                                     
 Reference tags:                                                                                                                                                                                     
 [istisnaa], [deferred_payment], [milestone_payment], [construction_contract], [turn_key]                                                                                                            
                                                                                                                                                                                                     
  
                                                               2. Post-Construction Ownership Transfer (Diminishing Musharaka, FAS 4)                                                                
                                                                                                                                                                                                     
 Key Compliance Points:                                                                                                                                                                              
                                                                                                                                                                                                     
  • Partnership, Buyback, and Leasing: Diminishing Musharaka lets ABC acquire financier’s share in phases, through a binding buyback promise—but not at original or face value.                      
  • Rental/Lease: Permitted on financier’s retained share, but only once ABC receives usable possession (i.e., when factory is operational).                                                         
  • No Pre-Operational Outflows: Rental or buyout obligations cannot trigger prior to project completion and operational handover.                                                                   
  • General Musharaka Rules: Partnership must follow all standard Sharikat al-‘Inan partnership conditions.                                                                                          
                                                                                                                                                                                                     
 Reference tags:                                                                                                                                                                                     
 [diminishing_musharakah], [diminishing_musharakah_rules], [diminishing_musharakah_equity_acquisition], [diminishing_musharakah_rent_lease], [ownership_transfer], [staged_buyout]                   
                                                                                                                                                                                                     
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
                                                                                 Overall Shariah Compliance Judgment                                                                                 
                                                                                                                                                                                                     
  • Istisnaa Phase: Fully Shariah-compliant if all operational, payment, and transfer mechanics conform as stated.                                                                                   
  • Diminishing Musharaka Phase: Structurally compliant per AAOIFI Shariah Standards, provided (i) staged buybacks are done above face value, (ii) rental/buyout only starts when asset is           
    operational, (iii) partnership rules are strictly followed.                                                                                                                                      
  • Integrated Flow: No riba, clear assignment of risk, and transaction independence at every phase are maintained.                                                                                  
                                                                                                                                                                                                     
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
 Conclusion:                                                                                                                                                                                         
 The proposed dual-phase Turn-Key Istisnaa + Diminishing Musharaka design, as described, is compliant with Shariah Standards (SS), conditional on meticulous adherence to the points above for each  
 phase in execution.                                                                                                                                                                                 
                                                                                                                                                                                                     
 If you require a copy-paste ready compliance reference for documentation or board purposes, let me know!                                                                                            
                                                                                                                                                                                                     
"""